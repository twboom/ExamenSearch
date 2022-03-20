const session = {
    disconnects: 0,
    initalized: false
};

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
    if (session.disconnects === 0) { renderInfo('CONNECTING', false) };
    const socket = new WebSocket(url);

    function handleOpen() {
        console.log('CLIENT:', 'WebSocket connection opened');
        session.disconnects = 0;
        if (!session.initalized) {
            renderInfo('READY', false);
            session.initalized = true;
        } else {
            renderInfo('CLEAR', false)
        }
    }

    function handleDisconnect() {
        session.disconnects++;
        if (session.disconnects === 1 && session.initalized) {
            renderInfo('CONNECTION_LOST', false);
            console.log('CLIENT:', 'WebSocket connection closed');
        } else {
            renderInfo('CONNECTION_FAILED', false);
            console.log('CLIENT:', 'WebSocket connection failed');
        }
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
                console.error('There was an server error: ' + data.data.message);
                renderInfo('ERROR', false);
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