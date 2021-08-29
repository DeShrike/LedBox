const VueApp = {
    data() {
        return {
            counter: 42,
            info: "",
            showArrows: false,
            socket: null,
            connected: false,
            server: null
        }
    },
    created() {
        this.server = "http://" + document.domain + ":" + location.port;
    },
    mounted() {
        setInterval(() => { this.counter++ }, 1000);

        this.addInfo("Connecting");
        this.socket = io.connect(this.server);
        const self = this;

        this.socket.on("Connected", function(msg) {
            self.addInfo("Connected");
            self.connected = true;
        }).on("connect", function(msg) {
            self.addInfo("connect");
            self.connected = false;
        }).on("disconnect", function(msg) {
            self.addInfo("disconnect");
            self.showCurrentAction("(not connected)");
            self.connected = false;
        }).on("reconnect", function(msg) {
            self.addInfo("reconnect");
            self.connected = false;
        }).on("reconnect_attempt", function(msg) {
            self.addInfo("reconnect_attempt");
            self.connected = false;
        }).on("reconnecting", function(msg) {
            self.addInfo("reconnecting");
            self.connected = false;
        }).on("reconnect_error", function(msg) {
            self.addInfo("reconnect_error");
            self.connected = false;
        }).on("LedBox", function(msg) {
            self.addInfo("LedBox");
            if (msg.random_loop) {
                self.showCurrentAction("Random - " + msg.active_plugin);
            }
            else {
                self.showCurrentAction(msg.active_plugin);
            }

            self.showArrows = msg.need_arrows;
       });
    },
    methods: {
        menuClick(action) {
            this.socket.emit("ActionEvent", { data: action });
        },
        specialClick(action) {
            this.socket.emit("SpecialEvent", { data: action });
        },
        arrowClick(arrow) {
            this.socket.emit("ArrowEvent", { data: arrow });
        },
        showCurrentAction(currentAction) {
            $("#current-action").html(currentAction);
        },
        addInfo(info) {
            this.info = this.info + " " + info;
        }
    }
};

Vue.createApp(VueApp).mount('#ledbox-vue');
