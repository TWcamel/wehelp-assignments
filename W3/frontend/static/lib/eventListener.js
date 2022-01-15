let customedAddEventListener = ({ element, data }) => {
	element.addEventListener("click", () => {
		createGalleryItemContainer(data, {
			from: 8,
			to: 16,
		});
		element.remove()
	});
};
