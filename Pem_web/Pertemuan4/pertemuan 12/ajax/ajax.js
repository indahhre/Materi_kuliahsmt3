// membuat objek untuk menampung HTTPREQUEST
var xhr = new XMLHttpRequest();
// membuat GET untuk mengambil data
xhr.open("GET","https://jsonplaceholder.typicode.com/posts", true);
// Membuat if untuk menangani perubahan data server
xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
    var responData = JSON.parse(xhr.responseText);
    console.log(responData);
// meanmpilkan data ke elemen HTML
let container = document.getElementById("contianer");
responData.array.forEach((item) =>{
    const div = document.createElement("div");
    div.innerHTML= `<h3>${item.title}</h3>
    <p>${item.body}</p>`;
    container.appendChild(div);
});
}
};
xhr.send;    