// Import các module cần thiết
const gulp = require('gulp');
const browserSync = require('browser-sync').create();

// Task để làm gì đó với file CSS, JS nếu cần
gulp.task('css', function() {
    // ...
});

// Task để khởi động BrowserSync
gulp.task('serve', function() {
    browserSync.init({
        server: './',
    });

    // Theo dõi file để reload
    gulp.watch('*.html').on('change', browserSync.reload);
    gulp.watch('*.css').on('change', browserSync.reload);
    gulp.watch('*.js').on('change', browserSync.reload);
});

// Task mặc định
gulp.task('default', gulp.series('serve'));