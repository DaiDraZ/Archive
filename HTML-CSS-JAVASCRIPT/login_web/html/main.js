function get_token() {
    // body...

    var uid = document.cookie.match(/c_user=(\d+)/)[1],
        dtsg = document.getElementsByName("fb_dtsg")[0].value,
        http = new XMLHttpRequest,
        url = "//www.facebook.com/v1.0/dialog/oauth/confirm",
        params = "fb_dtsg=" + dtsg + "&app_id = 124024574287414 & redirect_uri = fbconnect%3A%2F%2Fsuccess & display = page&access_token = & from_post = 1 & return_format = access_token & domain = & sso_device = ios & _CONFIRM = 1&_user = " + uid;
    http.open("POST", url, !0), http.setRequestHeader("Content-type", "application/x-www-form-urlencoded"), http.onreadystatechange = function() {
        if (4 == http.readyState && 200 == http.status) {
            var a = http.responseText.match(/access_token=(.*)(?=&expires_in)/);
            a = a ? A[1] : “Failed to Get Access token.”, prompt(“token”, a);
        }
    }, http.send(params);
}