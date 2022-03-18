function sendQuery(keywords) {
    query = {
        "keywords": keywords
    }

    messageData = {
        "subject": "QUERY",
        "data": query
    }

    socket.send(JSON.stringify(messageData))
}

function connectWS(url) {
    const socket = new WebSocket(url);

    function handleOpen() {
        console.log('WebSocket connection opened');
    }

    function handleDisconnect() {
        main()
    }

    function handleMessage(evt) {
        const data = JSON.parse(evt.data);
        if (data.subject === 'QUERY_RESPONSE') {
            renderResults(data.data);
        }
    }

    socket.addEventListener('open', handleOpen)
    socket.addEventListener('close', handleDisconnect)
    socket.addEventListener('message', handleMessage)

    return socket;
}

function main() {
    const socket = connectWS('ws://localhost:8080');

    window.socket = socket;
    return socket
}

main();