<template>
    <div class="hello">Hello {{who}}</div>
</template>

<script type="module">
const SeeksRelationGraph = require('relation-graph');
module.exports = {
    data: function() {
        return {
            who: 'world'
        }
    }
}
</script>

<style>
.hello {
    background-color: #ffe;
}
</style>