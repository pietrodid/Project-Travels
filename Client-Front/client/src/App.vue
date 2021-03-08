<template>
  <div id="app" class="container">
    
    <b-navbar toggleable="md" type="dark" variant="warning">
      
    <cabecera></cabecera>
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
        <b-navbar-brand href="#">Cordillera Travel Express</b-navbar-brand>

          <b-collapse is-nav id="nav_collapse">
        
            <b-navbar-nav>
              <b-nav-item :to="{name:'Home'}" exact>Home</b-nav-item> 
              <b-nav-item :to="{name:'Busqueda'}">Busqueda</b-nav-item>
              <b-nav-item :to="{name:'Contacto'}">Contacto</b-nav-item> 
            </b-navbar-nav>
          </b-collapse>            
    
    </b-navbar>
  <router-view/>
  </div>
</template>
<script>
import Cabecera from '@/components/Cabecera.vue'
import Contacto from '@/components/Contacto.vue'
import Busqueda from '@/components/Busqueda.vue'

export default {  
  name:'app',
  components:{
    Cabecera,
    Busqueda,
    Contacto
  }
}
</script>