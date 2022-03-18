function clearEverything(hideInfo=true) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';

    const statsContainer = document.getElementById('stats-container');
    statsContainer.innerHTML = '';

    const infoContainer = document.getElementById('info');
    infoContainer.innerHTML = '';
    if (hideInfo) { infoContainer.style.display = 'none' };
}

function renderStats(data) {
    const statsContainer = document.getElementById('stats-container');

    const stats = document.createElement('div');
    stats.id = 'stats';

    const totalResults = document.createElement('p');
    totalResults.innerText = `Totaal aantal resultaten: ${data.total_results}`;
    
    const totalDocuments = document.createElement('p');
    totalDocuments.innerText = `Totaal aantal documenten: ${data.total_files}`;

    stats.appendChild(totalResults);
    stats.appendChild(totalDocuments);

    statsContainer.appendChild(stats);
}

function renderInfo(subject, clear=true) {
    const container = document.getElementById('info');
    container.className = '';
    container.style.display = 'block';
    if (clear) {
        clearEverything(false)
    } else {
        container.innerHTML = '';
    }

    if (subject === 'CLEAR') {
        container.innerHTML = '';
        container.className = '';
        container.style.display = 'none';
    };

    const info = document.createElement('p');

    switch(subject) {
        case 'LOADING':
            info.innerText = 'Moment, we zijn de resultaten aan het verzamelen...';
            container.classList.add('information');
            break;

        case 'SENDING':
            info.innerText = 'Moment, we halen de resultaten op...'
            container.classList.add('information');
            break;

        case 'ERROR':
            info.innerText = 'Ojee, er is iets misgegaan...';
            container.classList.add('information');
            break;

        case 'NO_RESULTS':
            info.innerText = 'Ojee, we hebben helemaal niets gevonden!';
            container.classList.add('warning');
            break;
        
        case 'CONNECTING':
            info.innerText = 'Moment, we verbinden met de server...';
            container.classList.add('information');
            break;

        case 'READY':
            info.innerText = 'Begin met typen in het zoekveld!';
            container.classList.add('confirmation');
            break;

        case 'CONNECTION_LOST':
            info.innerText = 'We hebben de verbinding met de server verloren...';
            container.classList.add('warning');
            break;

        case 'CONNECTION_FAILED':
            info.innerText = 'We konden de server niet bereiken...';
            container.classList.add('error');
            break;
    }    

    container.appendChild(info);
}

function renderResults(data) {
    clearEverything();
    if (data.results.length == 0) { renderInfo('NO_RESULTS'); return };
    
    const resultsContainer = document.getElementById('results');

    const head = document.createElement('tr');
    const headExam = document.createElement('th');
    const headType = document.createElement('th');
    const headLink = document.createElement('th');

    headExam.innerText = 'Examen';
    headType.innerText = 'Type';
    headLink.innerText = 'Link';

    head.appendChild(headExam);
    head.appendChild(headType);
    head.appendChild(headLink);

    resultsContainer.appendChild(head);

    const results = data.results;
    results.forEach(result => {
        const capitalize = s => (s && s[0].toUpperCase() + s.slice(1)) || ""
        const subject = capitalize(result.subject);

        const container = document.createElement('tr');
        container.classList.add('result');

        const exam = document.createElement('td');
        exam.innerHTML = `${subject} ${result.level} ${result.year} (pagina ${result.page_number})`;
        container.appendChild(exam);

        const docType = document.createElement('td');
        docType.innerHTML = capitalize(result.document_type);
        container.appendChild(docType);

        const link = document.createElement('td');
        const linkEl = document.createElement('a');
        linkEl.target = '_blank';
        linkEl.href = result.url + '#page=' + result.page_number;
        linkEl.innerText = 'Ga naar pagina';
        link.appendChild(linkEl);
        container.appendChild(link);

        resultsContainer.appendChild(container);
    });

    renderStats(data);
}