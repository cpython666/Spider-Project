$(document).ready(function () {
    // Function to check if an element is in the current view
    function isElementPartiallyInViewport(el) {
        var rect = el.getBoundingClientRect();
        var windowHeight = window.innerHeight || document.documentElement.clientHeight;
        var windowWidth = window.innerWidth || document.documentElement.clientWidth;

        return (
            rect.bottom > 0 &&
            rect.right > 0 &&
            rect.top < windowHeight &&
            rect.left < windowWidth
        );
    }

    function handleScroll() {
        $('p,h1,h2,h3,ol,pre').each(function () {
            if (isElementPartiallyInViewport(this)) {
                $(this).removeClass('hidden');
            } else {
                $(this).addClass('hidden');
            }
        });
    }

    // 初始化时绑定滚动事件
    $(window).on('scroll', function () {
        handleScroll();
    });

    // 当页面获得焦点时
    $(window).on('focus', function () {
        console.log('获取焦点了');
        handleScroll();
        $(window).on('scroll', function () {
        handleScroll();
    });
    });

    // 当页面失去焦点时
    $(window).on('blur', function () {
        // 解绑滚动事件监听
        console.log('失去焦点了');
        $(window).off('scroll');
    });
});