let app = (() => {
    document.forms["user-login-form"].addEventListener("submit", (event) => {
        event.preventDefault();
        event.stopPropagation();
        fetch(event.target.action, {
            method: "POST",
            body: new URLSearchParams(new FormData(event.target)), // event.target is the form
        })
            .then((resp) => {
                if (resp.redirected) window.location.href = resp.url;
                return resp;
            })
            .catch((error) => {
                console.error(error);
            });
    });
    const fetchTest = async () => {
        return await fetch("https://www.google.com/", { mode: "cors" })
            .then((resp) => resp.json())
            .then((data) => console.log(data));
    };
    const xmlHttpRequestTest = async (url, callback) => {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = () => {
            if (xhr.readyState === 4) callback(xhr.response);
        };
        xhr.open("GET", url, true);
        xhr.send();
    };
    const testRequest = (() => {
        // fetchTest();
        xmlHttpRequestTest(
            "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json",
            () => {
                console.info("in callback function");
            }
        );
    })();
})();
