let memberHelper = (() => {
    document.forms["member-query-membership-form"].addEventListener(
        "submit",
        (event) => {
            event.preventDefault();
            event.stopPropagation();
            (async () => {
                const _data = await getMember(event);
                pushMemberMsg("query-membership-msg", _data, (nameTag = true));
            })();
        }
    );

    const getMember = async (event) => {
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

    modifyMemberName = async (event) => {
        try {
            return await fetch(event.target.action, {
                method: "POST",
                body: JSON.stringify({
                    name: event.target.children.username.value,
                }),
                headers: {
                    "content-type": "application/json",
                },
            })
                .then((resp) => resp.json())
                .then((data) => data);
        } catch (error) {
            console.error(error);
        }
    };

    const pushMemberMsg = (element, msg, nameTag = false) => {
        const dom = document.querySelector(`.${element}`);
        if (nameTag) dom.innerText = msg === null ? null : `${msg.name} `;
        else if (!nameTag) dom.innerText = msg === null ? null : `${msg}`;
    };

    document.forms["update-membership-name-form"].addEventListener(
        "submit",
        (event) => {
            event.preventDefault();
            event.stopPropagation();
            (async () => {
                const _data = await modifyMemberName(event);
                console.log(_data);
                let msg = "Fail to update your name";
                if (_data.ok) msg = "Successfully update your name";
                pushMemberMsg("update-membership-name-msg", msg);
            })();
        }
    );
})();
