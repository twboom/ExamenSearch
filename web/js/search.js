const input = document.getElementById('search-field');
const button = document.getElementById('search-button');

function search() {
    if (input.value.length == '') { return };
    let keywords = [input.value];
    sendQuery(keywords);
    console.log('CLIENT:', `Searching for "${keywords}"`);
}

function clearEverything() {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';

    const statsContainer = document.getElementById('stats-container');
    statsContainer.innerHTML = '';

    const infoContainer = document.getElementById('info');
    infoContainer.innerHTML = '';
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

function renderInfo(subject) {
    clearEverything();
    const infoContainer = document.getElementById('info');

    const info = document.createElement('p');

    switch(subject) {
        case 'LOADING':
            info.innerText = 'Moment, we zijn de resultaten aan het verzamelen...';
            break;

        case 'SENDING':
            info.innerText = 'Moment, we halen de resultaten op...'
    }    

    infoContainer.appendChild(info);
}

function renderNothing() {
    clearEverything();
    const resultsContainer = document.getElementById('results');

    const loading = document.createElement('tr');

    const loadingEl = document.createElement('td');
    loadingEl.colSpan = 3;
    loadingEl.innerText = 'Ojee, we hebben helemaal niets gevonden!';
    loading.appendChild(loadingEl);

    resultsContainer.appendChild(loading);
}

function renderResults(data) {
    clearEverything();
    if (data.results.length == 0) { renderNothing(); return };
    
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

button.addEventListener("click", search)
input.addEventListener("keypress", evt => {
    if (evt.key === 'Enter') {
        search();
    }
})
