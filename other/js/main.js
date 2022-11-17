function SubToMLSub() {
        document.getElementById("ltdz").value = Dz();
        document.getElementById("id4").value = Orange();
        document.getElementById("id5").value = MLS();
        Copy();
    } //原始订阅转换

function Dz() {
    let url = document.getElementById("url").value;
    let host = document.getElementById("host").value;
    let name = document.getElementById("name").value;
    let port = document.getElementById("port").value;
    if (url === ""||host === "") {
        alert("必填不能为空！");
    }else{
    let mlurl = "https://dy.hcnmb.cn/subscribe/&&" + url + "&&" + host + "&&";
    if (!!document.getElementById("name").value) {
        mlurl += name;
    }
    if (!!document.getElementById("port").value) {
        mlurl += "&&" + port;//多端口筛选
    }
    return mlurl;
    }
}

function Orange() {
    let url = document.getElementById("url").value;
    url = encodeURIComponent(url);
    let host = document.getElementById("host").value;
    if (url === ""||host === "") {
        alert("必填不能为空！");
    }else{
        return "https://api.orangeapi.org/sub?suburl=" + url + "&newhost=" + host;
    }
}

function MLS() {
    let url = document.getElementById("url").value;
    url = encodeURIComponent(url);
    let host = document.getElementById("host").value;
    let name = document.getElementById("name").value;
    let port = document.getElementById("port").value;
    if (url === ""||host === "") {
        alert("必填不能为空！");
    }else{
        let mlUrl = "http://zhuan.mlsao.ml/auto/?url=http%3A%2F%2Fzhuan.mlsao.ml%2Fsub%2F%3Fair_url%3D" + url + "%26host%3D" + host;
        if (!!document.getElementById("name").value) {
        mlUrl += "%26addname%3D" + name;
    } //备注
    if (!!document.getElementById("port").value) {
        mlUrl += "%26ports%3D" + port;//多端口筛选
    }
    return mlUrl;
    }
}

function Copy() {
    let Url2 = document.getElementById("id4").value;
    if (Url2) {
        navigator.clipboard.writeText(Url2).then(() => {
        }); // 执行浏览器复制命令
        alert("已复制好，可贴粘。");
    }
}
