var gulp = require('gulp');
var jshint = require('gulp-jshint');
var browserify = require('gulp-browserify');

gulp.task('default', function() {
    // place code for your default task here
});

gulp.task('lint', function() {
    return gulp.src('./js/**/*.js')
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

gulp.task('compile', function() {
    gulp.src('js/app.js')
        .pipe(browserify({
            insertGlobals : true,
            debug : true
        }))
        .pipe(gulp.dest('./build/js'))
});

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch('js/**/*.js', ['lint', 'compile']);
});