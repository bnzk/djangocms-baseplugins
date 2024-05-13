var gulp = require("gulp"),
  sass = require("gulp-sass"),
  jshint = require("gulp-jshint"),
  path = require("path"),
  rename = require("gulp-rename"),
  shell = require("gulp-shell"),
  dummy = "last";

// fix Promise() error from which package again?
require("es6-promise").polyfill();

gulp.task("jshint", function () {
  gulp.src(["gulpfile.js", "djangocms_baseplugins/**.js"]).pipe(jshint());
});

gulp.task("flake8", shell.task(["flake8 --ignore=errors"]));

gulp.task("default", ["sass", "jshint", "flake8"]);

gulp.task("watch", function () {
  gulp.watch(["gulpfile.js", "djangocms_misc/**.js"], ["jshint"]);
  gulp.watch(["**/**.py"], ["flake8"]);
});
