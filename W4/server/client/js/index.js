let app = (() => {
	document.forms["user-login-form"].addEventListener("submit", (event) => {
		event.preventDefault();
		fetch(event.target.action, {
			method: "POST",
			body: new URLSearchParams(new FormData(event.target)), // event.target is the form
		})
			.then((resp) => {
				resp.json().then((data) => console.log(data));
			})
			.catch((error) => {
				console.error(error);
			});
	});
})();
