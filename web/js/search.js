const input = document.getElementById('search-field');
const button = document.getElementById('search-button');

function search() {
    if (input.value.length == '') { return };
    let keywords = [input.value];
    sendQuery(keywords);
    console.log('searching for: ' + input.value);
}

function renderResults(data) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';
    const results = data.results
    results.forEach(result => {
        const capitalize = s => (s && s[0].toUpperCase() + s.slice(1)) || ""
        const subject = capitalize(result.subject);

        const container = document.createElement('div');
        container.classList.add('result');

        const exam = document.createElement('p');
        exam.innerHTML = `${subject} ${result.level} ${result.year}`;
        container.appendChild(exam);

        const link = document.createElement('p');
        const linkEl = document.createElement('a');
        linkEl.href = result.url + '#page=' + result.page_number;
        linkEl.innerText = 'Ga naar pagina';
        link.appendChild(linkEl);
        container.appendChild(link);

        resultsContainer.appendChild(container);
    });
}

button.addEventListener("click", search)
input.addEventListener("keypress", evt => {
    if (evt.key === 'Enter') {
        search();
    }
})
