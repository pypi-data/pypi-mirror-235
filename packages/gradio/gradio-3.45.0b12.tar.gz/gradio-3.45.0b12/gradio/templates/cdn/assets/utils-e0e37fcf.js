const r=t=>{let a=["B","KB","MB","GB","PB"],e=0;for(;t>1024;)t/=1024,e++;let n=a[e];return t.toFixed(1)+" "+n},l=()=>!0;function d(t,{autoplay:a}){async function e(){a&&await t.play()}return t.addEventListener("loadeddata",e),{destroy(){t.removeEventListener("loadeddata",e)}}}export{l as a,d as l,r as p};
//# sourceMappingURL=utils-e0e37fcf.js.map
