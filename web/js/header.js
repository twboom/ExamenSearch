window.addEventListener('scroll', _ => {
    if (document.body.scrollTop > 50) {
        document.getElementsByTagName('header')[0].classList.add('small');
    } else {
        document.getElementsByTagName('header')[0].classList.remove('small');
    }
})