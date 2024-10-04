document.addEventListener("DOMContentLoaded", function () {
  const previewDiv = document.getElementById("preview");
  const uploadFileInput = document.getElementById("uploadFile");
  const section = document.body.getAttribute("data-section");
  const localStorageKey = `backgroundImage_${section}`;

  const storedImage = localStorage.getItem(localStorageKey);
  if (storedImage) {
    setPreviewBackground(storedImage);
  }
  document.getElementById("fondo").addEventListener("click", function () {
    uploadFileInput.click();
  });

  uploadFileInput.addEventListener("change", function (e) {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (event) {
        const fileType = file.type;
        if (fileType.startsWith("image/")) {
          const imageUrl = event.target.result;
          setPreviewBackground(imageUrl);
          localStorage.setItem(localStorageKey, imageUrl);
        } else if (fileType === "application/pdf") {
          alert(
            "No se soporta PDF, pero puedes usar una librería como pdf.js para manejar PDFs."
          );
        }
      };
      reader.readAsDataURL(file);
    }
  });

  function convertToPercentage(value, total) {
    return (value / total) * 100;
  }

  function setPreviewBackground(imageUrl) {
    previewDiv.style.backgroundImage = `url(${imageUrl})`;
  }
  // Lógica de arrastre
  function dragElement(elmnt) {
    let pos1 = 0,
      pos2 = 0,
      pos3 = 0,
      pos4 = 0;

    elmnt.onmousedown = dragMouseDown;

    function dragMouseDown(e) {
      e.preventDefault();
      pos3 = e.clientX;
      pos4 = e.clientY;
      document.onmouseup = closeDragElement;
      document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
      e.preventDefault();
      pos1 = pos3 - e.clientX;
      pos2 = pos4 - e.clientY;
      pos3 = e.clientX;
      pos4 = e.clientY;

      const newTop = elmnt.offsetTop - pos2;
      const newLeft = elmnt.offsetLeft - pos1;

      const percentageTop = convertToPercentage(
        newTop,
        previewDiv.offsetHeight
      );
      const percentageLeft = convertToPercentage(
        newLeft,
        previewDiv.offsetWidth
      );

      elmnt.style.top = `${percentageTop}%`;
      elmnt.style.left = `${percentageLeft}%`;
    }

    function closeDragElement() {
      document.onmouseup = null;
      document.onmousemove = null;

      const id = elmnt.getAttribute("id");
      if (id) {
        const pos = {
          top: (elmnt.offsetTop / previewDiv.offsetHeight) * 100 + "%",
          left: (elmnt.offsetLeft / previewDiv.offsetWidth) * 100 + "%",
        };
        localStorage.setItem(`textPosition_${id}`, JSON.stringify(pos));
      }
    }
  }

  previewDiv.addEventListener("dblclick", function () {
    // Añadir un texto editable al hacer doble clic en la preview
    const text = prompt("Ingrese el texto a agregar:");
    if (text) {
      addDraggableText(text);
    }
  });

  function numberToWords(num) {
    // Función para convertir números a palabras (0-9999 en español)
    const units = [
      "",
      "uno",
      "dos",
      "tres",
      "cuatro",
      "cinco",
      "seis",
      "siete",
      "ocho",
      "nueve",
      "diez",
      "once",
      "doce",
      "trece",
      "catorce",
      "quince",
      "dieciséis",
      "diecisiete",
      "dieciocho",
      "diecinueve",
    ];
    const tens = [
      "",
      "",
      "veinte",
      "treinta",
      "cuarenta",
      "cincuenta",
      "sesenta",
      "setenta",
      "ochenta",
      "noventa",
    ];
    const hundreds = [
      "",
      "ciento",
      "doscientos",
      "trescientos",
      "cuatrocientos",
      "quinientos",
      "seiscientos",
      "setecientos",
      "ochocientos",
      "novecientos",
    ];

    if (num === 0) return "cero";
    if (num === 100) return "cien";
    if (num < 20) return units[num];
    if (num < 100)
      return (
        tens[Math.floor(num / 10)] +
        (num % 10 !== 0 ? " y " + units[num % 10] : "")
      ).trim();
    if (num < 1000)
      return (
        hundreds[Math.floor(num / 100)] +
        (num % 100 !== 0 ? " " + numberToWords(num % 100) : "")
      ).trim();
    if (num < 10000) {
      const thousand = Math.floor(num / 1000);
      const rest = num % 1000;
      return (
        (thousand === 1 ? "mil" : units[thousand] + " mil") +
        (rest !== 0 ? " " + numberToWords(rest) : "")
      );
    }
    return "";
  }

  function formatDateToText(dateStr) {
    // Función para convertir la fecha en formato de texto
    const months = [
      "enero",
      "febrero",
      "marzo",
      "abril",
      "mayo",
      "junio",
      "julio",
      "agosto",
      "septiembre",
      "octubre",
      "noviembre",
      "diciembre",
    ];
    const [year, month, day] = dateStr.split("-").map((num) => parseInt(num));

    const dayText = numberToWords(day);
    const yearText = numberToWords(year);
    const monthText = months[month - 1];

    return `${
      dayText.charAt(0).toUpperCase() + dayText.slice(1)
    } de ${monthText} de ${yearText}`;
  }

  // Función para añadir textos por defecto a la vista previa con posiciones
  function addDefaultTexts() {
    const currentDate = new Date();
    currentDate.setHours(currentDate.getHours() - 5);
    const currentDateStr = currentDate.toISOString().split("T")[0]; // YYYY-MM-DD format

    const [year, month, day] = currentDateStr.split("-");

    const dayText = new Intl.NumberFormat("es-ES", { style: "decimal" }).format(
      day
    );
    const yearText = new Intl.NumberFormat("es-ES", {
      style: "decimal",
    }).format(year);
    const months = [
      "enero",
      "febrero",
      "marzo",
      "abril",
      "mayo",
      "junio",
      "julio",
      "agosto",
      "septiembre",
      "octubre",
      "noviembre",
      "diciembre",
    ];
    const monthText = months[parseInt(month) - 1];

    if (section === "bautizo") {
      addDraggableText(`${day}`, 62.68922528940338, 59.57178841309824, "diab");
      addDraggableText(`${dayText}`, 79.60819234194123, 19.64735516372796, "diaab");
      addDraggableText(`${monthText}`, 62.42208370436332, 70.40302267002518, "mesb");
      addDraggableText(`${monthText}`, 79.69723953695458, 28.085642317380355, "messb");
      addDraggableText(`${year}`, 62.51113089937667, 87.02770780856423, "annob");
      addDraggableText(`${yearText}`, 79.60819234194123, 44.7103274559194, "annoob");
    } else if (section === "matrimonio") {
      addDraggableText(`${day}`, 68.6553873552983, 61.96473551637279, "diam");
      addDraggableText(`${dayText}`, 83.17008014247551, 18.261964735516372, "diaam");
      addDraggableText(`${monthText}`, 68.83348174532502, 70.52896725440806, "mesm");
      addDraggableText(`${monthText}`, 83.17008014247551, 26.322418136020154, "messm");
      addDraggableText(`${year}`, 68.83348174532502, 86.90176322418137, "annom");
      addDraggableText(`${yearText}`, 83.34817453250223, 43.45088161209068, "annoom");
    } else if (section === "confirmacion") {
      addDraggableText(`${day}`, 96.61620658949242, 48.740554156171285, "diac");
      addDraggableText(`${monthText}`, 96.70525378450579, 61.83879093198993, "mesc");
      addDraggableText(`${year - 2020}`, 96.79430097951915, 87.1536523929471, "annoc");
    } else if (section === "pricomunion") {
      addDraggableText(`${day}`, 95.10240427426537, 52.39294710327456, "diap");
      addDraggableText(`${monthText}`, 95.013357079252, 64.73551637279597, "mesp");
      addDraggableText(`${year - 2000}`, 95.10240427426537, 84.25692695214106, "annop");
    }
  }
  function addDraggableText(text, top = 0, left = 0, id = null) {
    const previewDiv = document.getElementById("preview");
    const textElement = document.createElement("div");

    textElement.classList.add("text-draggable");
    textElement.contentEditable = true;
    textElement.innerText = text;

    id = id || `text_${Date.now()}`;
    textElement.setAttribute("id", id);

    const storedPos = localStorage.getItem(`textPosition_${id}`);
    if (storedPos) {
      const { top: storedTop, left: storedLeft } = JSON.parse(storedPos);
      textElement.style.top = storedTop;
      textElement.style.left = storedLeft;
    } else {
      textElement.style.top = `${convertToPercentage(
        top,
        previewDiv.offsetHeight
      )}%`;
      textElement.style.left = `${convertToPercentage(
        left,
        previewDiv.offsetWidth
      )}%`;
    }

    previewDiv.appendChild(textElement);
    dragElement(textElement);

    textElement.addEventListener("mouseup", function () {
      const currentPos = {
        top: `${convertToPercentage(
          textElement.offsetTop,
          previewDiv.offsetHeight
        )}%`,
        left: `${convertToPercentage(
          textElement.offsetLeft,
          previewDiv.offsetWidth
        )}%`,
      };
      localStorage.setItem(`textPosition_${id}`, JSON.stringify(currentPos));
    });
  }

  function transferFormDataToPreview() {
    // Function to transfer form data to preview - Bautismo
    if (section === "bautizo") {
      const formFields = {
        parroquia: document.querySelector('[name="parroquia"]').value,
        libro: document.querySelector('[name="libro"]').value,
        fojas: document.querySelector('[name="fojas"]').value,
        numero: document.querySelector('[name="numero"]').value,
        apellidos: document.querySelector('[name="apellidos"]').value,
        nombres: document.querySelector('[name="nombres"]').value,
        padre: document.querySelector('[name="padre"]').value,
        madre: document.querySelector('[name="madre"]').value,
        lugar_nacimiento: document.querySelector('[name="lugar_nacimiento"]')
          .value,
        fechaNacimiento: document.querySelector('[name="fecha_nacimiento"]')
          .value,
        fechaBautizo: document.querySelector('[name="fecha_bautizo"]').value,
        padrinos: document.querySelector('[name="padrinos"]').value,
        oficiante: document.querySelector('[name="oficiante"]').value,
        anotaciones: document.querySelector('[name="anotaciones"]').value,
      };

      const fechaNacimiento = formatDateToText(formFields.fechaNacimiento);
      const fechaBautizo = formatDateToText(formFields.fechaBautizo);

      addDraggableText(`${formFields.parroquia}`, 23.15227070347284, 33.6272040302267, "parroquia");
      addDraggableText(`${formFields.libro}`, 25.022261798753338, 57.556675062972296, "libro");
      addDraggableText(`${formFields.fojas}`, 25.022261798753338, 71.91435768261965, "fojas");
      addDraggableText(`${formFields.numero}`, 24.844167408726626, 82.7455919395466, "numero");
      addDraggableText(`${formFields.apellidos}`, 29.207479964381122, 19.143576826196472, "apellidos");
      addDraggableText(`${formFields.nombres}`, 31.70080142475512, 18.513853904282115, "nombres");
      addDraggableText(`${formFields.padre}`, 33.74888691006233, 33.123425692695214, "padre");
      addDraggableText(`${formFields.madre}`, 35.8860195903829, 32.99748110831234, "madre");
      addDraggableText(`${formFields.lugar_nacimiento}`, 38.11219946571683, 45.34005037783375, "lugar_nacimiento");
      addDraggableText(`${fechaNacimiento}`, 40.516473731077475, 38.16120906801007, "fechaNacimiento");
      addDraggableText(`${fechaBautizo}`, 44.879786286731964, 36.14609571788413, "fechaBautizo");
      addDraggableText(`${formFields.padrinos}`, 49.33214603739982, 18.89168765743073, "padrinosb");
      addDraggableText(`${formFields.oficiante}`, 51.46927871772039, 19.143576826196472, "oficiante");
      addDraggableText(`${formFields.anotaciones}`, 53.78450578806767, 30.730478589420656, "anotaciones");
    } else if (section === "matrimonio") {
      const formFields = {
        parroquia: document.querySelector('[name="parroquia"]').value,
        libro: document.querySelector('[name="libro"]').value,
        fojas: document.querySelector('[name="fojas"]').value,
        numero: document.querySelector('[name="numero"]').value,
        esposo: document.querySelector('[name="esposo"]').value,
        padre_esposo: document.querySelector('[name="padre_esposo"]').value,
        madre_esposo: document.querySelector('[name="madre_esposo"]').value,
        lugar_bautizo_esposo: document.querySelector(
          '[name="lugar_bautizo_esposo"]'
        ).value,
        esposa: document.querySelector('[name="esposa"]').value,
        padre_esposa: document.querySelector('[name="padre_esposa"]').value,
        madre_esposa: document.querySelector('[name="madre_esposa"]').value,
        lugar_bautizo_esposa: document.querySelector(
          '[name="lugar_bautizo_esposa"]'
        ).value,
        fecha_matrimonio: document.querySelector('[name="fecha_matrimonio"]')
          .value,
        padrinos: document.querySelector('[name="padrinos"]').value,
        anotaciones: document.querySelector('[name="anotaciones"]').value,
      };

      const fecham = formatDateToText(formFields.fecha_matrimonio);

      addDraggableText(`${formFields.parroquia}`, 18.2546749777382, 32.61964735516373, "parroquiam");
      addDraggableText(`${formFields.libro}`, 20.837043633125557, 57.556675062972296, "librom");
      addDraggableText(`${formFields.fojas}`, 20.7479964381122, 72.29219143576826, "fojasm");
      addDraggableText(`${formFields.numero}`, 20.837043633125557, 84.25692695214106, "numerom");
      addDraggableText(`${formFields.esposo}`, 25.467497773820124, 14.483627204030228, "esposo");
      addDraggableText(`${formFields.padre_esposo}`, 27.78272484416741, 18.387909319899247, "padre_esposo");
      addDraggableText(`${formFields.madre_esposo}`, 30.45414069456812, 14.73551637279597, "madre_esposo");
      addDraggableText(`${formFields.lugar_bautizo_esposo}`, 32.94746215494212, 32.61964735516373, "lugar_bautizo_esposo");
      addDraggableText(`${formFields.esposa}`, 35.35173642030276, 14.86146095717884, "esposa");
      addDraggableText(`${formFields.padre_esposa}`, 37.93410507569012, 18.1360201511335, "padre_esposa");
      addDraggableText(`${formFields.madre_esposa}`, 40.338379341050754, 14.987405541561714, "madre_esposa");
      addDraggableText(`${formFields.lugar_bautizo_esposa}`, 42.920747996438116, 33.37531486146096,"lugar_bautizo_esposa");
      addDraggableText(`${fecham}`, 45.59216384683882, 35.642317380352644, "fecham");
      addDraggableText(`${formFields.padrinos}`, 50.48975957257347, 16.3727959697733, "padrinos");
      addDraggableText(`${formFields.anotaciones}`, 55.56544968833482, 27.95969773299748, "anotacionesm");
    } else if (section === "confirmacion") {
      const formFields = {
        parroquia: document.querySelector('[name="parroquia"]').value,
        nombre: document.querySelector('[name="nombre"]').value,
        ex_monsenor: document.querySelector('[name="ex_monsenor"]').value,
        fecha: document.querySelector('[name="fecha"]').value,
        padres: document.querySelector('[name="padres"]').value,
        padrinos: document.querySelector('[name="padrinos"]').value,
      };

      const fechac = formatDateToText(formFields.fecha);

      addDraggableText(`${formFields.nombre}`, 44.52359750667854, 38.41309823677582, "nombrec");
      addDraggableText(`${formFields.ex_monsenor}`, 62.2439893143366, 24.937027707808564, "ex_monsenor");
      addDraggableText(`${formFields.parroquia}`, 66.25111308993766, 22.16624685138539, "parroquiac");
      addDraggableText(`${formFields.padres}`, 70.43633125556545, 18.89168765743073, "padresc");
      addDraggableText(`${formFields.padrinos}`, 74.17631344612646, 20.277078085642316, "padrinosc");
      addDraggableText(`${fechac}`, 78.6286731967943, 17.632241813602015, "fechac");
    } else if (section === "pricomunion") {
      const formFields = {
        parroquia: document.querySelector('[name="parroquia"]').value,
        nombre: document.querySelector('[name="nombre"]').value,
        fecha: document.querySelector('[name="fecha"]').value,
        padre: document.querySelector('[name="padre"]').value,
        madre: document.querySelector('[name="madre"]').value,
      };

      const [day, month, year] = formFields.fecha.split("-");
      const months = [
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre",
      ];
      const monthText = months[parseInt(month) - 1];

      addDraggableText(`${formFields.parroquia}`, 77.64915405164737, 33.6272040302267, "parroquiap");
      addDraggableText(`${formFields.nombre}`, 57.969723953695464, 35.012594458438286, "nombrep");
      addDraggableText(`${formFields.padre}`, 82.19056099732859, 27.83375314861461, "padrep");
      addDraggableText(`${formFields.madre}`, 82.27960819234195, 62.97229219143576, "madrep");
      addDraggableText(`${day}`, 71.95013357079252, 79.59697732997482, "dayp");
      addDraggableText(`${monthText}`, 72.12822796081923, 59.06801007556675, "monthp");
      addDraggableText(`${year}`, 71.86108637577917, 43.702770780856426, "yearp");
    }
  }

  document
    .getElementById("previewButton")
    .addEventListener("click", transferFormDataToPreview); // Event listener for preview button

  window.onload = function () {
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (key.startsWith("textPosition_")) {
        const id = key.split("_")[1];
        const storedPos = JSON.parse(localStorage.getItem(key));
        addDraggableText("", storedPos.top, storedPos.left, id);
      }
    }
    addDefaultTexts();
  };
});
