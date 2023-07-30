async function getHallOfFame() {
    var url = "/api/user.php?action=hall_of_fame";
    var response = await fetch(url);
    return await response.json();
}


function main() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const page = urlParams.get('page');

    let pageIndex = parseInt(page) - 1;
    let itemsPerPage = 5;

    document.getElementById("page-number").innerHTML = "Page " + page;

    getHallOfFame().then(function (data) {
        document.getElementById("hof-body").innerHTML = '';
        for (i = pageIndex * itemsPerPage; i < ((pageIndex * itemsPerPage) + itemsPerPage) && i < data["message"].length; i++) {
            let elem = data["message"][i];
            tr = document.createElement("tr");
            for (attr in elem) {
                td = document.createElement("td");
                td.innerText = elem[attr];
                tr.appendChild(td);
            }
            td = document.createElement("td");
            view = document.createElement("a");
            view.href = `/view.php?id=${elem['id']}`;
            view.innerText = "View";
            td.appendChild(view);
            tr.appendChild(td);
            document.getElementById("hof-body").appendChild(tr);
        }
    });
}

main();