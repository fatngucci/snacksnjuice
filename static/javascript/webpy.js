(function init(){
    'use strict';

    let q1 = document.getElementById("quote1")
    let q2 = document.getElementById("quote2")
    let q3 = document.getElementById("quote3")

    console.log(q1)

    let qs = [q1, q2, q3];

    console.log(qs)

    qs.forEach(q => {
        console.log(q.dataset)
        console.log(q.dataset.section);
    })
    console.log(qs)
    function loadDiv(etnries){
        const[entry] = etnries;

        if(entry.isIntersecting){
            console.log(entry.target);
            entry.target.classList.add('loadVisible');
        } else {
            entry.target.classList.remove('loadVisible');
        }
    }

    const options = {
        root: null,
        rootMargin: '0px',
        threshold: .2
    }

    const observer = new IntersectionObserver(loadDiv, options);

    qs.forEach(q => {
        observer.observe(q);
    })

})();