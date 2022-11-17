function SubToMLSub() {
    document.getElementById("id4").value = Sub();
    document.getElementById("id5").value = Short();
    Copy();
} //原始订阅转换

function Sub() {
    let url = document.getElementById("url").value;
    let host = document.getElementById("host").value;
    let name = document.getElementById("name").value;
    let port = document.getElementById("port").value;
    if (url === "") {
        alert("必填不能为空！");
    } else {
        let mlUrl = window.location.href + "subscribe/&&" + url;
        if (!!document.getElementById("host").value) {
        mlurl += "&&" + host;
    }
        if (!!document.getElementById("name").value) {
        mlurl += "&&" + name;
    }
        if (!!document.getElementById("port").value) {
        mlurl += "&&" + port;//多端口筛选
    }
        return mlurl;
    }
}

function Short() {
    return document.getElementById("id4").value;
}

function Copy() {
    let Url2 = document.getElementById("id4").value;
    if (Url2) {
        navigator.clipboard.writeText(Url2).then(() => {
        }); // 执行浏览器复制命令
        alert("已复制好，可贴粘。");
    }
}
