let requestURL = async (url) => {
	try {
		return await fetch(url).then((response) => response.json()).then((data) => data.result);
	} catch (error) {
		console.error("Error:", error);
	}
};