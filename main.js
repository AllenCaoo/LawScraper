function formdata() {
    let input = document.getElementById("firstname").value.toLowerCase().replace(/\s/g, "");
    alert(input);
    let input = document.getElementById("lastname").value.toLowerCase().replace(/\s/g, "");
    alert(input);
    let input = document.getElementById("email").value.toLowerCase().replace(/\s/g, "");
    alert(input);
}