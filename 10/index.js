function foo1(d) {
  const last = function() {
    console.log("Called on last index " + d);
  };

  const stop = d > 9 ? last : ++d;
  foo2(d, stop);
}

function foo2(d, cb) {
  console.log("This is foo2", d);
  (function() {
    if (typeof cb == "function") {
      cb();
      return;
    }
    foo1(d);
  })();
}

foo1(0);
