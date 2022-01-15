let appendChildDOM = (parent, childName, DOM) => {
	let dom = document.createElement(`${DOM.type}`);
	if (DOM.type === "img") {
		parent.appendChild(dom);
	} else {
		dom.classList.add(childName);
		parent.appendChild(dom);
	}
	setDivProperty(dom, childName, DOM.option);
};

let setDivProperty = (DOM, domName, option) => {
	if (domName === "gallery-items-title") {
		DOM.innerText = option;
	} else if (domName === "gallery-items-img") {
		DOM.src = `${option}`;
		DOM.alt = "";
	}
};

let createGalleryItemContainer = (data, { from, to }) => {
	let gallery = document.querySelector(".gallery");

	for (let i = from; i < to; i++)
		appendChildDOM(gallery, "gallery-items", { type: "div" });

	document.querySelectorAll(".gallery-items").forEach((item, idx) => {
		if (idx >= from && idx < to)
			createGalleryItems({ container: item, idx: from + idx }, data);
	});

	console.log("//////////////////////////");
};

let createGalleryItems = ({ container, idx }, data) => {
	(async () => {
		await data.then((data) => {
			appendChildDOM(container, "gallery-items-img", {
				type: "img",
				option: splitJPG(data.results[idx].file),
			});
			appendChildDOM(container, "gallery-items-title", {
				type: "div",
				option: data.results[idx].stitle,
			});
		});
	})();
};
