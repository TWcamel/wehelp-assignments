let errorHelper = (() => {
	const getErrorMessage = () =>
		decodeURIComponent(window.location.search).substring(9);
	const removeDOMFirstChild = (element) => {
		const dom = document.querySelector(`${element}`);
		dom.removeChild(dom.firstElementChild);
	};
	const pushDOMMsg = (element, msg) => {
		const dom = document.querySelector(`${element}`);
		const children = document.createElement("h4");
		dom.appendChild(children);
		children.innerText = `${msg} 🐒`;
	};

	removeDOMFirstChild(".main-page");
	pushDOMMsg(".main-page", getErrorMessage());
})();
