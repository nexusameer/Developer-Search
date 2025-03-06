
//GET SEARCH FORM AND PAGE LINKS
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

//ENSURE SEARCH FORM EXISTS
if (searchForm) {
    for (let i = 0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault()

            //GET THE DATA ATTRIBUTE
            let page = this.dataset.page

            //ADD HIDDEN SEARCH INPUT TO FORM
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`


            //SUBMIT FORM
            searchForm.submit()
        })
    }
}



let tags = document.getElementsByClassName('project-tag')

for (let i = 0; tags.length > i; i++) {
    tags[i].addEventListener('click', (e) => {
        let tagId = e.target.dataset.tag
        let projectId = e.target.dataset.project

        // console.log('TAG ID:', tagId)
        // console.log('PROJECT ID:', projectId)

        fetch('http://127.0.0.1:8000/api/remove-tag/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'project': projectId, 'tag': tagId })
        })
            .then(response => response.json())
            .then(data => {
                e.target.remove()
            })

    })
}
//Delete Button Javascript
    document.getElementById("deleteForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the form from submitting
        // Handle form submission here, e.g., show confirmation dialog
    });

    document.getElementById("backButton").addEventListener("click", function(event) {
        event.preventDefault(); // Prevent the default action of the link (going back)
        // Handle going back here, e.g., redirect to the desired page
        window.location.href = "{% url 'profiles' %}";
    });