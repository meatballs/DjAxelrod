var gulp = require('gulp');
var concat = require('gulp-concat');
var sass   = require('gulp-sass');
var minifyCss = require('gulp-minify-css');


var STATIC_DEV = "./static-dev/";

gulp.task('scripts', function() {
  return gulp.src([
  		'lib/jquery/dist/jquery.js', 
  		'lib/d3.min.js', 
  		'lib/bootstrap-sass-official/assets/javascripts/bootstrap.min.js', 
  		'lib/modernizr/modernizr.js', 
  		], {cwd: STATIC_DEV})
    .pipe(concat('scripts.js'))
    .pipe(gulp.dest('./static/'));
});

gulp.task('sass', function() {
  return gulp.src(STATIC_DEV + 'scss/main.scss')
  	.pipe(sass())
    .pipe(minifyCss())
    .pipe(gulp.dest('./static/'))
});

// remove all the csv stuff after we add in the csv api
gulp.task('csv', function() {
  return gulp.src('**.*.csv').pipe(gulp.dest(STATIC_DEV));
});

gulp.task('default', ['sass', 'scripts', 'csv'], function() {
    gulp.watch([STATIC_DEV + '**/*.scss', STATIC_DEV + '**/*.js', STATIC_DEV + '**/*.csv'], ['sass', 'scripts', 'csv']);
});