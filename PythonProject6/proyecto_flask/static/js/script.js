// script.js

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("fileInput").addEventListener("change", uploadFile);
});

function uploadFile() {
    let fileInput = document.getElementById("fileInput");
    let file = fileInput.files[0];
    if (!file) {
        alert("Por favor, seleccione un archivo.");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("Error: " + data.error);
        } else {
            document.getElementById("media").textContent = data.media;
            document.getElementById("mediana").textContent = data.mediana;
            document.getElementById("desviacion").textContent = data.desviacion;
            document.getElementById("suma").textContent = data.suma;
            showPopup();
        }
    })
    .catch(error => {
        alert("Hubo un error al procesar el archivo.");
        console.error(error);
    });
}

function showPopup() {
    document.getElementById("resultPopup").style.display = "block";
}

function closePopup() {
    document.getElementById("resultPopup").style.display = "none";
}
