fetch("https://jsonplaceholder.typicode.com/posts").then((Response) => {
    if (!Response.ok) {
        throw new Error("Response not ok");
    }
    return response.json();
}).then((data) => {
    console.log(data);
}).catch((error) => {
console.error("Error:", error);});