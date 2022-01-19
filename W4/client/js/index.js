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
})();
