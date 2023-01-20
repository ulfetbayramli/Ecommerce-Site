let form = document.getElementById("login-form")
form.addEventListener('submit', async function(event) {

    let postData = {
        username: form.username.value,
        password: form.password.value
    }

    let response = await fetch(`${location.origin}/api/token/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(postData)
    })

    if (response.ok) {
        let data = await response.json()
        localStorage.setItem('user-detail', JSON.stringify(data))
        
    }
})