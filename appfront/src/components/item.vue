<template>
    <li class="process" :class="className">
      <slot></slot>
    </li>
</template>

<script>
    export default {
        name: "item",
        props: ["childMsg"],
        computed: {
          className: function() {
            console.log(this.childMsg);
            if (this.childMsg === "data") {
              return "process-data";
            } else if (this.childMsg === "alg") {
              return "process-alg";
            } else if (this.childMsg === "model"){
              return "process-model";
            } else {
              return "process-result";
            }
          }
        }
    }
</script>

<style scoped>
  .process {
    font-size: 12px;
    width: 12rem;
    height: 4rem;
    line-height: 4rem;
    margin: 2px auto;
    position: relative;
    border-radius: 5%;
    background-color: #f4f4f4;
    text-align: center;
    box-shadow: 1px 1px 1px #337ab7;
    list-style-type: none;
  }
  .process:before {
    content: "";
    width: 1.8rem;
    height: 0.9rem;
    margin: 0;
    position: absolute;
    top: 0rem;
    left: 5rem;
    border-radius: 0 0 0.9rem 0.9rem;
    background-color: #ffffff;
    box-shadow: 1px 1px 1px #333;
    z-index: 0;
  }
  .process:after {
    content: "";
    width: 1.8rem;
    height: 0.9rem;
    border-radius: 0 0 0.9rem 0.9rem;
    position: absolute;
    top: 4rem;
    left: 5rem;
    /* border-radius: 50%; */
    background-color: #f4f4f4;
    box-shadow: 1px 1px 1px #333;
    z-index: 1;
  }
  .process.process-data:before {
    box-shadow: 1px 1px 1px #00a65a;
  }
  .process.process-data,
  .process.process-data:after {
    box-shadow: 1px 1px 1px #00a65a;
    background-color: #5ac594;
    color: #fff;
  }
  .process.process-alg,
  .process.process-alg:after {
    box-shadow: 1px 1px 1px #337ab7;
    background-color: #81b5d4;
    color: #fff;
  }
  .process.process-eva,
  .process.process-eva:after {
    box-shadow: 1px 1px 1px #f39c12;
    background-color: #f7bf66;
    color: #fff;
  }
  .process.process-model,
  .process.process-model:after {
    box-shadow: 1px 1px 1px #dd4b39;
    background-color: #e57f72;
    color: #fff;
  }
  .process.process-result,
  .process.process-result:after {
    box-shadow: 1px 1px 1px #00c0ef;
    background-color: #5ad6f5;
    color: #fff;
  }

</style>
