import asyncio
import json
import threading

import javascript
from javascript import On, console, eval_js
from javascript import globalThis as js
from javascript import require


def demo1():
    """
    Access JavaScript from Python.

    https://github.com/extremeheat/JSPyBridge#access-javascript-from-python
    """
    chalk, fs = require("chalk"), require("fs")

    print("Hello", chalk.red("world!"), "it's", js.Date().toLocaleString())
    fs.writeFileSync("HelloWorld.txt", "hi!")


def demo2():
    """
    Do something with stdlib's `JSON` serializer.

    https://github.com/extremeheat/JSPyBridge/blob/master/examples/python/nbt.py
    """
    JSON = js.JSON
    obj = {"hello": "world"}
    outcome = JSON.stringify(obj)
    print("outcome:", outcome)
    console.error("outcome:", outcome)


def demo3():
    """
    Evaluate chunks of JavaScript code.

    https://github.com/extremeheat/JSPyBridge/blob/master/docs/python.md#expression-evaluation
    """

    countUntil = 9
    myArray = [1]
    myObject = {"hello": ""}

    # Make sure you await everywhere you expect a JS call !
    output = eval_js(
        """
        myObject['world'] = 'hello'    
        for (let x = 0; x < countUntil; x++) {
            await myArray.append(2)
        }
        return 'it worked'
    """
    )
    print("output:", output)
    print("countUntil:", countUntil)
    print("myArray:", myArray)
    print("myObject:", myObject)


async def demo4():
    """
    Run a Node-RED instance.

    https://github.com/oyajiDev/NodeRED.py/blob/master/noderedpy/node-red-starter/index.js
    https://github.com/node-red/node-red/blob/master/packages/node_modules/node-red/red.js
    """
    express = require("express")
    http = require("http")
    red = require("node-red")
    fs = require("fs")
    path = require("path")

    # Create Express and Node-RED server.
    express_app = express()
    red_server = http.createServer(express_app)

    # Set configs.
    editor_theme = {}
    # editor_theme = json.load(open("editorTheme.json"))
    editor_theme["projects"] = {
        "enabled": False,
    }

    # Initialize Node-RED.
    user_categories = []
    default_categories = user_categories.append(
        ["subflows", "common", "function", "network", "sequence", "parser", "storage"]
    )
    settings = {
        "editorTheme": editor_theme,
        "httpAdminRoot": "./var/nodered",
        "httpNodeRoot": "/",
        "flowFile": "noderedpy.json",
        "userDir": "./var/nodered",
        "paletteCategories": "",
        "verbose": True,
        "uiHost": "0.0.0.0",
        "uiPort": 1880,
    }
    red.init(red_server, settings)

    # Node-RED default routes.
    express_app.use("/", express.static("web"))
    express_app.use(red.settings.httpAdminRoot, red.httpAdmin)
    express_app.use(red.settings.httpNodeRoot, red.httpNode)

    red.log.info("Starting 1")

    foo = red.start(print)
    print("foo:", foo)
    print("red.then:", red.then)
    # javascript.events.
    # await asyncio.sleep(3)
    red.log.info("Starting 2")
    server = red_server.listen(1880, "0.0.0.0")
    await asyncio.sleep(10)
    # print("server:", server)
    # await server.then()
    red.log.info("Stopping")
    # await asyncio.wait(asyncio.Future())
    # all_tasks = asyncio.all_tasks()
    # print("all_tasks:", all_tasks)
    # await asyncio.wait(all_tasks)

    return

    startjs = """
// start node-red
function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}
function f1() {
    console.log("F1");
    setTimeout(f1, 10000);
}

async function run() {
    console.log("RUN");

    red.start().then(() => {
        console.log("YES-1");
        await red_server.listen(1880, "0.0.0.0", () => {
            red.log.info("RED running!");
            console.log("YES-2");
            //sleep(10000);
            setTimeout(f1, 10000);
            //await sleep(10000);
            console.log("YES-3");
            //fs.writeFileSync(path.join(__dirname, "started"), "");
        });
    });

    console.log("END")
}
run();
/*
red.start().then(() => {
    console.log("YES-1");
    red_server.listen(1880, "0.0.0.0", () => {
        console.log("YES-2");
        //sleep(10000);
        setTimeout(f1, 10000);
        console.log("YES-3");
        //fs.writeFileSync(path.join(__dirname, "started"), "");
    });
});
*/


    """
    retval = javascript.eval_js(startjs)
    red.log.info("Starting 2")
    print("retval:", retval)

    all_tasks = asyncio.all_tasks()
    print("all_tasks:", all_tasks)
    await asyncio.wait(all_tasks)

    return

    # Start Node-RED.
    red.log.info("Starting 1")
    # red.on("foo", print)
    # javascript.On(red, print)
    # red.events.on("then", lambda: print("============== FOFFOOFOF"))
    # print("red:", red)
    foo = red.start(print)
    print("foo:", foo)
    print("red.then:", red.then)
    # javascript.events.
    red.log.info("Starting 2")
    server = red_server.listen(1880, "0.0.0.0")
    # print("server:", server)
    # await server.then()
    red.log.info("Starting 3")
    # await asyncio.wait(asyncio.Future())
    all_tasks = asyncio.all_tasks()
    print("all_tasks:", all_tasks)
    await asyncio.wait(all_tasks)
    return
    loop = asyncio.get_event_loop()
    loop.run_forever()
    # threading.Event().wait()
    # thing = asyncio.wait(asyncio.Future())
    # asyncio.run(thing)
    red.log.info("Starting 4")


def demo5():
    javascript.eval_js("module.exports = { forty_two: function() { foo(); } };")


if __name__ == "__main__":
    # demo1()
    # demo2()
    # demo3()
    # asyncio.run(demo4())
    demo5()
