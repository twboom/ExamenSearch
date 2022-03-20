const input = document.getElementById('search-field');
const button = document.getElementById('search-button');

function search() {
    if (input.value.length == '') { return };
    let keywords = input.value.split(';');
    keywords = keywords.map(keyword => keyword.trim());
    sendQuery(keywords);
    console.log('CLIENT:', `Searching for "${keywords}"`);
};

button.addEventListener("click", search);
input.addEventListener("keypress", evt => {
    if (evt.key === 'Enter') {
        search();
    };
});
