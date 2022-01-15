import "./lib/createElements.js";
import "./lib/request.js";
import "./lib/eventListener.js";

let app;
(app = () => {
	const req =
		"https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
	const data = requestURL(req);

	createGalleryItemContainer(data, {
		from: 0,
		to: 8,
	});

	const btnSection = document.querySelector("#gallery-load-more");
	customedAddEventListener({ element: btnSection, data: data });
})();
