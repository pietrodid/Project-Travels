<template>
  <div>
    <b-container>
      <hr />

      <h1 class="text-primary">Busqueda Online</h1>
      <br />
      <div>
        <p><strong>Saliendo De: </strong></p>
        <b-form-select v-model="origen" class="mb-3" >
         <b-form-select-option :value="id" v-for="item in terminales" :key="item.direccion">
            {{ item.direccion }}
              </b-form-select-option>
        </b-form-select>
      </div>
      <div class="mt-2">
        Origen: <strong>{{ origen }}</strong>
      </div>
      <br />
      <div>
        <p><strong>Voy A:</strong></p>
        <b-form-select v-model="destino" class="mb-3" >
         <b-form-select-option :value="id" v-for="item in terminales" :key="item.direccion">
            {{ item.direccion }}
              </b-form-select-option>
        </b-form-select>
      </div>
      <div class="mt-2">
        Destino: <strong>{{ destino }}</strong>
      </div>
      <br />
      <div>
        
        <b-form-group label="Fecha de su Viaje">
          <b-form-radio-group
            v-model="state"
            aria-controls="ex-disabled-readonly"
          >
            <b-form-radio value="disabled">Solo Ida</b-form-radio>
            <b-form-radio value="radonly">Ida Y Vuelta</b-form-radio>
          </b-form-radio-group>
        </b-form-group>
        <b-form-datepicker
          id="datepicker-placeholder"
          placeholder="Día De Salida"
        ></b-form-datepicker>
        <b-form-datepicker
          id="ex-disabled-readonly"
          placeholder="Día De Retorno"
          :disabled="disabled"
          :readonly="readonly"
        ></b-form-datepicker>
      </div>
      <br />
      <div>
        <b-button variant="outline-primary">Buscar</b-button>
      </div>
    </b-container>
  </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker';
import { Global } from "../Global";
import axios from "axios";
export default {
  name: "terminal",
  data() {
    return {
      origen: "",
      destino: "",
      selected2: "",
      state: "disabled",
      terminales: [],
      trayectos: []  
    };
  },
  mounted() {
    this.getTerminal();
    this.getTrayecto();
  },
  methods: {
    getTerminal() {
      let config = {
        Headers: {
          token: Global.token,
        },
      };
      axios.get(Global.url + "terminal", config).then((res) => {
        //console.log('terminal', res.status)
        if (res.status == 200) {
          this.terminales = res.data;
          console.log("res", res);
        } else {
          alert("no se puede conectar");
        }
      });
    }, getTrayecto() {    
      let config = {
        Headers: {
          token: Global.token,
        },
      };
      axios.get(Global.url + "trayecto", config).then((res) => {
        //console.log('terminal', res.status)
        if (res.status == 200) {
          this.trayecto = res.data;
          console.log("res", res);
        } else {
          alert("no se puede conectar");
        }
      });
    },
  },
  computed: {
    disabled() {
      return this.state === "disabled";
    },
    readonly() {
      return this.state === "readonly";
    },
  },
};
</script>
