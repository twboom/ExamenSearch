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
        console.log('CLIENT:', 'WebSocket connection opened');
    }

    function handleDisconnect() {
        main()
    }

    function handleMessage(evt) {
        const data = JSON.parse(evt.data);

        console.log('SERVER:', data);
        
        switch(data.subject) {
            case 'QUERY_RESULTS':
                renderResults(data.data);
                break;
            
            case 'QUERY_LOADING':
                renderInfo('LOADING');
                break;

            case 'QUERY_SENDING':
                renderInfo('SENDING');	
                break;

            case 'ERROR':
                alert('There was an error: ' + data.data.message);
                break;
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