function foo1(d) {
  const stop = d == 9;
  const last = d => {
    console.log("Called on last index " + d);
  };

  const callback = stop ? last(d + 1) : null;
  if (!stop) foo2(++d, callback);
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
