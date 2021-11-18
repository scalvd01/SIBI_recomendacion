var express = require("express");
var app = express();
var cors = require("cors");
const neo4j = require("neo4j-driver");
const driver = neo4j.driver(
  "bolt://localhost:7687",
  neo4j.auth.basic("neo4j", "1234")
);

app.use(express.json()); //para procesamiento de json

app.use(cors());

app.set("port", process.env.PORT || 5000); //se usará el puerto que proporcione el servicio cloud/S.O./máquina servidor y sino el 8080

//Ponemos a escuchar el servidor
app.listen(app.get("port"), () => {
  console.log(
    "El servidor se encuentra escuchando en el puerto",
    app.get("port")
  );
});

app.get("/", (req, res) => {
  res.send("home del servidor\nFuncionando");
});

/*
app.get("/getDatosSteppers", function (request, response) {
  console.log("entrado en request datos de steppers");

  var queries = ["MATCH (n:n_display_size) RETURN n",
    "MATCH (n:Capacidad_bateria) RETURN n",
    "MATCH (n:n_ram) RETURN n",
    "MATCH (n:n_camera_pixels) RETURN n",
    "MATCH (n:expansion) RETURN n",
    "MATCH (n:os) RETURN n",
    "MATCH (n:brand_name) RETURN n",
  ];

  

  var datos = [];

  queries.forEach(function (element, i) {
    const session = driver.session();

    const resultPromise = session.run(element);
    console.log(element)

    resultPromise
      .then((result) => {
        datos.push(result.records);
        //console.log(datos.length);
        if (datos.length == 7) {
          response.send(datos);
        }
        session.close();
      })
      .catch((error) => {
        // handle error
        console.log(error);
        session.close();
      });
  });
});*/


app.post("/runQuery", function (request, response) {
  console.log("ejecutando " + request.body.query);

  var query = request.body.query;
  var name = request.body.name;
  console.log(query);

  var datos = [];

  const session = driver.session();

  const resultPromise = session.run(query);

  resultPromise
    .then((result) => {
      datos = result.records;
      var clean = [];
      datos.forEach((element) => {
        element.forEach((element1) => {
          console.log(element1.properties);
          clean.push(element1.properties[name]);
        });
      });
      response.send(clean);

      session.close();
    })
    .catch((error) => {
      // handle error
      console.log(error);
      session.close();
    });
});
