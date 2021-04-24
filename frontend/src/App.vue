<template>
 <div class="page">
    <div id="map" class="map" ref="map" style="width: 1000px;height: 1000px;">
    </div>
  </div>
</template>

<script>
import RelationChart from 'relation-chart'

export default {
  data () {
    return {}
  },
  mounted() {
    new RelationChart(this.$refs.map, data)
  },
}

</script>

<style>

</style>
