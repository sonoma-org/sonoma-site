const req = new Request("/api/projects")

async function reps() {
    var res = await fetch(req)
    const repos = document.getElementById("repos")
    var f = await res.json()

    for (let obj of f) {
        const new_req = new Request("/projects/" + obj)
        var new_res = await fetch(new_req)
        let element = document.createElement("div")
        element.innerHTML = await new_res.text()
        repos.append(element)
    }
}

reps()