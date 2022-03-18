window.addEventListener('scroll', _ => {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        document.getElementById('header').classList.add('small');
    } else {
        document.getElementById('header').classList.remove('small');
    }
})