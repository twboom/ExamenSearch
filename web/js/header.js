window.addEventListener('scroll', _ => {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        document.getElementById('header').classList.add('small');
        document.getElementById('main').classList.add('small');
    } else {
        document.getElementById('header').classList.remove('small');
        document.getElementById('main').classList.remove('small');
    }
})