const VueApp = {
    data() {
        return {
            counter: 42,
            msg: ""
        }
    },
    mounted() {
        setInterval(() => {
            this.counter++
        }, 1000)
    },
    methods: {
        menuClick(action) {
            this.msg = action;
        },
        arrowClick(action) {
            this.msg = action;
        }
    }
};

Vue.createApp(VueApp).mount('#ledbox-vue');
/*
var LedBox = (function() {
    "use strict";

    var socket = null;
    var connected = false;
    var server;

    function addInfo(msg)
    {
        var html = $(".info-block").html();
        html = html + " " + msg;
        $(".info-block").html(html);
    }

    function init() {

        addInfo("Init");
        $(".special-button").on("click", specialButton);
        $(".arrow-button").on("click", arrowButton);
        $(".action-button").on("click", actionButton);

        $(".arrow-button").hide();

        server = "http://" + document.domain + ":" + location.port;
        addInfo("Connecting");
        socket = io.connect(server);

        // connect error disconnect reconnect reconnect_attempt reconnecting reconnect_error

        socket.on("Connected", function(msg) {
            console.log("Connected", msg);
            addInfo("Connected");
            connected = true;
        }).on("connect", function(msg) {
            console.log("connect", msg);
            addInfo("connect");
            connected = false;
        }).on("disconnect", function(msg) {
            console.log("disconnect", msg);
            addInfo("disconnect");
            showCurrentAction("(not connected)");
            connected = false;
        }).on("reconnect", function(msg) {
            console.log("reconnect", msg);
            addInfo("reconnect");
            connected = false;
        }).on("reconnect_attempt", function(msg) {
            console.log("reconnect_attempt", msg);
            addInfo("reconnect_attempt");
            connected = false;
        }).on("reconnecting", function(msg) {
            console.log("connecting", msg);
            addInfo("reconnecting");
            connected = false;
        }).on("reconnect_error", function(msg) {
            console.log("reconnect_error", msg);
            addInfo("reconnect_error");
            connected = false;
        }).on("LedBox", function(msg) {
            console.log("LedBox event", msg);
            addInfo("LedBox");
            if (msg.random_loop) {
                showCurrentAction("Random - " + msg.active_plugin);
            }
            else {
                showCurrentAction(msg.active_plugin);
            }

            if (msg.need_arrows) {
                $(".arrow-button").show();
            }
            else {
                $(".arrow-button").hide();
            }
        });

        // setTimeout(2000, startWithoutSockets);
    }

    // // function startWithoutSockets() {
    // //     if (connected) {
    // //         return;
    // //     }

    // //     Ajax.request("/ledbox/state", "GET", null, function(resp) {
    // //         addInfo(resp);
    // //     },
    // //     function() {

    // //     });
    // // }

    function specialButton(e) {
        var action = $(this).data("action");
        console.log("Special", action);
        socket.emit("SpecialEvent", { data: action });
    }

    function arrowButton(e) {
        var arrow = $(this).data("arrow");
        console.log("Arrow", arrow);
        socket.emit("ArrowEvent", { data: arrow });
    }

    function actionButton(e) {
        var action = $(this).data("action");
        console.log("Action", action);
        socket.emit("ActionEvent", { data: action });
    }

    function showCurrentAction(currentAction) {
        $("#current-action").html(currentAction);
    }

    return {
        init: init,
    };
})();
*/