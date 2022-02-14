let memberHelper = (() => {
    document.forms["member-query-membership-form"].addEventListener(
        "submit",
        (event) => {
            event.preventDefault();
            event.stopPropagation();
            (async () => {
                const _data = await getMember(event);
                pushMemberMsg("query-membership-msg", _data);
            })();
        }
    );

    getMember = async (event) => {
        try {
            return await fetch(
                `${event.target.action}?username=${event.target.children.username.value}`,
                { method: "GET" }
            )
                .then((resp) => resp.json())
                .then((data) => data.data);
        } catch (error) {
            console.error(error);
        }
    };

    pushMemberMsg = (element, msg) => {
        const dom = document.querySelector(`.${element}`);
        dom.innerText = msg === null ? null : `${msg.name} 🐒`;
    };
})();
