"use strict";
(self["webpackChunk_datalayer_jupyter_ssh"] = self["webpackChunk_datalayer_jupyter_ssh"] || []).push([["lib_jupyterlab_index_js"],{

/***/ "../../../node_modules/css-loader/dist/cjs.js!./style/base.css":
/*!*********************************************************************!*\
  !*** ../../../node_modules/css-loader/dist/cjs.js!./style/base.css ***!
  \*********************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../../../node_modules/css-loader/dist/runtime/cssWithMappingToString.js */ "../../../node_modules/css-loader/dist/runtime/cssWithMappingToString.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../../../node_modules/css-loader/dist/runtime/api.js */ "../../../node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
// Imports


var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default()));
// Module
___CSS_LOADER_EXPORT___.push([module.id, ".dla-Container {\n    overflow-y: visible;\n}\n", "",{"version":3,"sources":["webpack://./style/base.css"],"names":[],"mappings":"AAAA;IACI,mBAAmB;AACvB","sourcesContent":[".dla-Container {\n    overflow-y: visible;\n}\n"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "../../../node_modules/css-loader/dist/cjs.js!./style/index.css":
/*!**********************************************************************!*\
  !*** ../../../node_modules/css-loader/dist/cjs.js!./style/index.css ***!
  \**********************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../../../node_modules/css-loader/dist/runtime/cssWithMappingToString.js */ "../../../node_modules/css-loader/dist/runtime/cssWithMappingToString.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../../../node_modules/css-loader/dist/runtime/api.js */ "../../../node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! -!../../../../node_modules/css-loader/dist/cjs.js!./base.css */ "../../../node_modules/css-loader/dist/cjs.js!./style/base.css");
// Imports



var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default()));
___CSS_LOADER_EXPORT___.i(_node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_2__["default"]);
// Module
___CSS_LOADER_EXPORT___.push([module.id, "\n", "",{"version":3,"sources":[],"names":[],"mappings":"","sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "../../icons/react/data1/esm/LaptopSimpleIcon.js":
/*!*******************************************************!*\
  !*** ../../icons/react/data1/esm/LaptopSimpleIcon.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);


const sizeMap = {
  "small": 16,
  "medium": 32,
  "large": 64
};

function LaptopSimpleIcon({
  title,
  titleId,
  size,
  colored,
  ...props
}, svgRef) {
  return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0__.createElement("svg", Object.assign({
    xmlns: "http://www.w3.org/2000/svg",
    className: "icon",
    viewBox: "0 0 1024 1024",
    fill: colored ? 'currentColor' : (['#fff', '#fffff', 'white', '#FFF', '#FFFFFF'].includes('currentColor') ? 'white' : 'currentColor'),
    width: size ? typeof size === "string" ? sizeMap[size] : size : "16px",
    "aria-hidden": "true",
    ref: svgRef,
    "aria-labelledby": titleId
  }, props), title ? /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0__.createElement("title", {
    id: titleId
  }, title) : null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0__.createElement("path", {
    d: "M956.9 845.1L896.4 632V168c0-17.7-14.3-32-32-32h-704c-17.7 0-32 14.3-32 32v464L67.9 845.1C60.4 866 75.8 888 98 888h828.8c22.2 0 37.6-22 30.1-42.9zM200.4 208h624v395h-624V208zm228.3 608l8.1-37h150.3l8.1 37H428.7zm224 0l-19.1-86.7c-.8-3.7-4.1-6.3-7.8-6.3H398.2c-3.8 0-7 2.6-7.8 6.3L371.3 816H151l42.3-149h638.2l42.3 149H652.7z"
  }));
}
const ForwardRef = react__WEBPACK_IMPORTED_MODULE_0__.forwardRef(LaptopSimpleIcon);
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (ForwardRef);

/***/ }),

/***/ "../../icons/react/data1/esm/LaptopSimpleIconLabIcon.js":
/*!**************************************************************!*\
  !*** ../../icons/react/data1/esm/LaptopSimpleIconLabIcon.js ***!
  \**************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components_lib_icon_labicon__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components/lib/icon/labicon */ "../../../node_modules/@jupyterlab/ui-components/lib/icon/labicon.js");
/* harmony import */ var _LaptopSimpleIcon_svg__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./LaptopSimpleIcon.svg */ "../../icons/react/data1/esm/LaptopSimpleIcon.svg");


const laptopSimpleIconLabIcon = new _jupyterlab_ui_components_lib_icon_labicon__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: '@datalayer/icons:laptop-simple',
    svgstr: _LaptopSimpleIcon_svg__WEBPACK_IMPORTED_MODULE_1__,
});
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (laptopSimpleIconLabIcon);

/***/ }),

/***/ "../../icons/react/eggs/esm/PirateSkull2Icon.js":
/*!******************************************************!*\
  !*** ../../icons/react/eggs/esm/PirateSkull2Icon.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);


const sizeMap = {
  "small": 16,
  "medium": 32,
  "large": 64
};

function PirateSkull2Icon({
  title,
  titleId,
  size,
  colored,
  ...props
}, svgRef) {
  return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0__.createElement("svg", Object.assign({
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: "0 0 512 512",
    fill: colored ? 'currentColor' : (['#fff', '#fffff', 'white', '#FFF', '#FFFFFF'].includes('currentColor') ? 'white' : 'currentColor'),
    "aria-hidden": "true",
    width: size ? typeof size === "string" ? sizeMap[size] : size : "16px",
    ref: svgRef,
    "aria-labelledby": titleId
  }, props), title ? /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0__.createElement("title", {
    id: titleId
  }, title) : null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0__.createElement("path", {
    d: "M256 31.203c-96 .797-117.377 76.692-79.434 135.133-6.397 6.534-10.344 15.886-.566 25.664 16 16 32 16 39.852 32.42h80.296C304 208 320 208 336 192c9.778-9.778 5.831-19.13-.566-25.664C373.377 107.896 352 32 256 31.203zm-42.146 101.049c.426-.003.862.007 1.306.03 28.404 1.442 40.84 59.718-10.83 51.095-10.412-1.738-17.355-50.963 9.524-51.125zm84.292 0c26.88.162 19.936 49.387 9.524 51.125C256 192 268.436 133.724 296.84 132.28c.444-.022.88-.032 1.306-.03zM32 144c7.406 88.586 64.475 175.544 156.623 236.797 17.959-7.251 35.767-15.322 50.424-23.877C180.254 319.737 104.939 255.465 32 144zm448 0C359.2 328.605 231.863 383.797 183.908 400.797c3.177 5.374 5.997 10.98 8.711 16.432 3.878 7.789 7.581 15.251 11.184 20.986A517.457 517.457 0 00256 417.973l.168.076a884.617 884.617 0 009.652-4.65C391.488 353.263 471.156 249.79 480 144zm-224 27.725l20.074 40.15L256 199.328l-20.074 12.547L256 171.725zm-65.604 57.11l15.76 51.042s31.268 24.92 49.844 24.92 49.844-24.92 49.844-24.92l15.76-51.041-27.086 19.236-8.063 16.248S267.35 279.547 256 279.547c-11.35 0-30.455-15.227-30.455-15.227l-8.063-16.248-27.086-19.236zm-59.984 152.976a32.548 32.548 0 00-2.375.027l.856 17.978c6.36-.302 10.814 2.416 16.11 8.64 5.298 6.222 10.32 15.707 15.24 25.589 4.918 9.882 9.707 20.12 16.122 28.45 6.415 8.327 16.202 15.446 27.969 13.89l-2.36-17.844c-4.094.541-6.78-1.099-11.349-7.031-4.57-5.933-9.275-15.46-14.268-25.489-4.992-10.029-10.297-20.604-17.644-29.234-6.888-8.09-16.556-14.686-28.3-14.976zm251.176 0c-11.745.29-21.413 6.885-28.3 14.976-7.348 8.63-12.653 19.205-17.645 29.234-4.993 10.03-9.698 19.556-14.268 25.489-4.57 5.932-7.255 7.572-11.35 7.031l-2.359 17.844c11.767 1.556 21.554-5.563 27.969-13.89 6.415-8.33 11.204-18.568 16.123-28.45 4.919-9.882 9.94-19.367 15.238-25.59 5.297-6.223 9.75-8.941 16.111-8.639l.856-17.978a32.853 32.853 0 00-2.375-.027zm-55.928 18.107c-13.97 10.003-30.13 18.92-47.424 27.478a524.868 524.868 0 0029.961 10.819c3.603-5.735 7.306-13.197 11.184-20.986 2.714-5.453 5.534-11.058 8.71-16.432-.77-.273-1.62-.586-2.43-.879zm-191.808 23.371l-27.67 10.352 7.904 31.771 36.424-11.707c-1.418-2.814-2.81-5.649-4.207-8.457-4.048-8.131-8.169-15.961-12.451-21.959zm244.296 0c-4.282 5.998-8.403 13.828-12.45 21.959-1.399 2.808-2.79 5.643-4.208 8.457l36.424 11.707 7.904-31.771-27.67-10.352zM78.271 435.438a9.632 9.632 0 00-1.32.12 6.824 6.824 0 00-1.217.313c-11.544 4.201-25.105 18.04-21.648 29.828 3.07 10.472 19.675 13.359 30.492 11.916 3.828-.51 8.415-3.761 12.234-7.086l-8.124-32.648c-3.238-1.285-7.214-2.528-10.417-2.443zm355.458 0c-3.203-.085-7.179 1.158-10.416 2.443l-8.125 32.648c3.819 3.325 8.406 6.576 12.234 7.086 10.817 1.443 27.422-1.444 30.492-11.916 3.457-11.788-10.104-25.627-21.648-29.828a6.824 6.824 0 00-1.217-.312 9.632 9.632 0 00-1.32-.122z"
  }));
}
const ForwardRef = react__WEBPACK_IMPORTED_MODULE_0__.forwardRef(PirateSkull2Icon);
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (ForwardRef);

/***/ }),

/***/ "./lib/SSH.js":
/*!********************!*\
  !*** ./lib/SSH.js ***!
  \********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-runtime */ "../../../node_modules/react/jsx-runtime.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/ThemeProvider.js");
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/BaseStyles.js");
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/Box/Box.js");
/* harmony import */ var _primer_react_drafts__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @primer/react/drafts */ "../../../node_modules/@primer/react/lib-esm/UnderlineNav2/index.js");
/* harmony import */ var _datalayer_icons_react__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @datalayer/icons-react */ "../../icons/react/data1/esm/LaptopSimpleIcon.js");
/* harmony import */ var _jupyterlab_handler__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./jupyterlab/handler */ "./lib/jupyterlab/handler.js");
/* harmony import */ var _state__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./state */ "./lib/state/index.js");
/* harmony import */ var _tabs_ImagesTab__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./tabs/ImagesTab */ "./lib/tabs/ImagesTab.js");
/* harmony import */ var _tabs_ContainersTab__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./tabs/ContainersTab */ "./lib/tabs/ContainersTab.js");
/* harmony import */ var _tabs_AboutTab__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./tabs/AboutTab */ "./lib/tabs/AboutTab.js");










const JupyterSSH = (props) => {
    const { setTab, getIntTab } = (0,_state__WEBPACK_IMPORTED_MODULE_2__["default"])();
    const intTab = getIntTab();
    const [version, setVersion] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)('');
    (0,react__WEBPACK_IMPORTED_MODULE_1__.useEffect)(() => {
        (0,_jupyterlab_handler__WEBPACK_IMPORTED_MODULE_3__.requestAPI)('config')
            .then(data => {
            setVersion(data.version);
        })
            .catch(reason => {
            console.error(`Error while accessing the jupyter server jupyter_ssh extension.\n${reason}`);
        });
    }, []);
    return ((0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.Fragment, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_4__["default"], { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_5__["default"], { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)(_primer_react__WEBPACK_IMPORTED_MODULE_6__["default"], { children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_6__["default"], { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_7__.UnderlineNav, { "aria-label": "docker", children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_7__.UnderlineNav.Item, { "aria-label": "images", "aria-current": intTab === 0 ? "page" : undefined, onSelect: e => { e.preventDefault(); setTab(0.0); }, children: "Images" }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_7__.UnderlineNav.Item, { "aria-label": "containers", "aria-current": intTab === 1 ? "page" : undefined, onSelect: e => { e.preventDefault(); setTab(1.0); }, children: "Containers" }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_7__.UnderlineNav.Item, { "aria-label": "about", "aria-current": intTab === 2 ? "page" : undefined, icon: () => (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_datalayer_icons_react__WEBPACK_IMPORTED_MODULE_8__["default"], { colored: true }), onSelect: e => { e.preventDefault(); setTab(2.0); }, children: "About" })] }) }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)(_primer_react__WEBPACK_IMPORTED_MODULE_6__["default"], { m: 3, children: [intTab === 0 && (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_tabs_ImagesTab__WEBPACK_IMPORTED_MODULE_9__["default"], {}), intTab === 1 && (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_tabs_ContainersTab__WEBPACK_IMPORTED_MODULE_10__["default"], {}), intTab === 2 && (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_tabs_AboutTab__WEBPACK_IMPORTED_MODULE_11__["default"], { version: version })] })] }) }) }) }));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (JupyterSSH);


/***/ }),

/***/ "./lib/jupyterlab/handler.js":
/*!***********************************!*\
  !*** ./lib/jupyterlab/handler.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "requestAPI": () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'jupyter_ssh', // API Namespace
    endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.log('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}


/***/ }),

/***/ "./lib/jupyterlab/index.js":
/*!*********************************!*\
  !*** ./lib/jupyterlab/index.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IJupyterSSH": () => (/* binding */ IJupyterSSH),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _datalayer_icons_react_data1_LaptopSimpleIconLabIcon__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @datalayer/icons-react/data1/LaptopSimpleIconLabIcon */ "../../icons/react/data1/esm/LaptopSimpleIconLabIcon.js");
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./handler */ "./lib/jupyterlab/handler.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./widget */ "./lib/jupyterlab/widget.js");
/* harmony import */ var _state__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ../state */ "./lib/state/index.js");
/* harmony import */ var _timer_TimerView__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../timer/TimerView */ "./lib/timer/TimerView.js");
/* harmony import */ var _state_mobx__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ../state/mobx */ "./lib/state/mobx.js");
/* harmony import */ var _style_index_css__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../../style/index.css */ "./style/index.css");












const IJupyterSSH = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@datalayer/jupyter-ssh:plugin');
/**
 * The command IDs used by the plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.create = 'create-jupyter-ssh-widget';
})(CommandIDs || (CommandIDs = {}));
/**
 * Initialization data for the @datalayer/jupyter-ssh extension.
 */
const plugin = {
    id: '@datalayer/jupyter-ssh:plugin',
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.ICommandPalette],
    optional: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__.ISettingRegistry, _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__.ILauncher, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_1__.ILayoutRestorer],
    provides: IJupyterSSH,
    activate: (app, palette, settingRegistry, launcher, restorer) => {
        const { commands } = app;
        const command = CommandIDs.create;
        const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.WidgetTracker({
            namespace: 'jupyter-ssh',
        });
        if (restorer) {
            void restorer.restore(tracker, {
                command,
                name: () => 'jupyter-ssh',
            });
        }
        const jupyterSSH = {
            timer: new _state__WEBPACK_IMPORTED_MODULE_6__.Timer(),
            TimerView: _timer_TimerView__WEBPACK_IMPORTED_MODULE_7__.TimerView,
            mobxTimer: _state_mobx__WEBPACK_IMPORTED_MODULE_8__.mobxTimer,
            MobxTimerView: _state_mobx__WEBPACK_IMPORTED_MODULE_8__.MobxTimerView,
        };
        commands.addCommand(command, {
            caption: 'Show SSH',
            label: 'SSH',
            icon: _datalayer_icons_react_data1_LaptopSimpleIconLabIcon__WEBPACK_IMPORTED_MODULE_9__["default"],
            execute: () => {
                const content = new _widget__WEBPACK_IMPORTED_MODULE_10__.JupyterSSHWidget(app, jupyterSSH);
                const widget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.MainAreaWidget({ content });
                widget.title.label = 'SSH';
                widget.title.icon = _datalayer_icons_react_data1_LaptopSimpleIconLabIcon__WEBPACK_IMPORTED_MODULE_9__["default"];
                app.shell.add(widget, 'main');
                tracker.add(widget);
            }
        });
        const category = 'Datalayer';
        palette.addItem({ command, category });
        if (launcher) {
            launcher.add({
                command,
                category,
                rank: 2.3,
            });
        }
        if (settingRegistry) {
            settingRegistry
                .load(plugin.id)
                .then(settings => {
                console.log('@datalayer/jupyter-ssh settings loaded:', settings.composite);
            })
                .catch(reason => {
                console.error('Failed to load settings for @datalayer/jupyter-ssh.', reason);
            });
        }
        (0,_handler__WEBPACK_IMPORTED_MODULE_11__.requestAPI)('config')
            .then(data => {
            console.log(data);
        })
            .catch(reason => {
            console.error(`Error while accessing the jupyter server jupyter_ssh extension.\n${reason}`);
        });
        console.log('JupyterLab plugin @datalayer/jupyter-ssh is activated!');
        return jupyterSSH;
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/jupyterlab/widget.js":
/*!**********************************!*\
  !*** ./lib/jupyterlab/widget.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "JupyterSSHWidget": () => (/* binding */ JupyterSSHWidget)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-runtime */ "../../../node_modules/react/jsx-runtime.js");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _datalayer_jupyter_react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @datalayer/jupyter-react */ "webpack/sharing/consume/default/@datalayer/jupyter-react/@datalayer/jupyter-react");
/* harmony import */ var _datalayer_jupyter_react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_datalayer_jupyter_react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _SSH__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../SSH */ "./lib/SSH.js");




class JupyterSSHWidget extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ReactWidget {
    _app;
    _jupyterSSH;
    constructor(app, jupyterSSH) {
        super();
        this._app = app;
        this._jupyterSSH = jupyterSSH;
        this.addClass('dla-Container');
    }
    render() {
        return ((0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.Fragment, { children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(this._jupyterSSH.TimerView, {}), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(this._jupyterSSH.MobxTimerView, { mobxTimer: this._jupyterSSH.mobxTimer }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_SSH__WEBPACK_IMPORTED_MODULE_3__["default"], { adapter: _datalayer_jupyter_react__WEBPACK_IMPORTED_MODULE_2__.JupyterLabAppAdapter.create(this._app) })] }));
    }
}


/***/ }),

/***/ "./lib/state/index.js":
/*!****************************!*\
  !*** ./lib/state/index.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Timer": () => (/* binding */ Timer),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   "useStore": () => (/* binding */ useStore)
/* harmony export */ });
/* harmony import */ var zustand__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! zustand */ "webpack/sharing/consume/default/zustand/zustand");
/* harmony import */ var zustand__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(zustand__WEBPACK_IMPORTED_MODULE_0__);

class Timer {
    _secondsPassed = 0;
    constructor() {
    }
    reset() {
        this._secondsPassed = 0;
    }
    increaseTimer() {
        this._secondsPassed += 1;
    }
    get secondsPassed() {
        return this._secondsPassed;
    }
}
const useStore = (0,zustand__WEBPACK_IMPORTED_MODULE_0__.create)((set, get) => ({
    tab: 0.0,
    getIntTab: () => Math.floor(get().tab),
    setTab: (tab) => set((state) => ({ tab })),
    timer: new Timer(),
    increaseTimer: () => {
        get().timer.increaseTimer();
        set((state) => ({ secondsPassed: get().timer.secondsPassed }));
    },
    secondsPassed: 0,
}));
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (useStore);


/***/ }),

/***/ "./lib/state/mobx.js":
/*!***************************!*\
  !*** ./lib/state/mobx.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "MobxTimer": () => (/* binding */ MobxTimer),
/* harmony export */   "MobxTimerView": () => (/* binding */ MobxTimerView),
/* harmony export */   "mobxTimer": () => (/* binding */ mobxTimer)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-runtime */ "../../../node_modules/react/jsx-runtime.js");
/* harmony import */ var mobx__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx */ "webpack/sharing/consume/default/mobx/mobx?346a");
/* harmony import */ var mobx__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var mobx_react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! mobx-react */ "webpack/sharing/consume/default/mobx-react/mobx-react");
/* harmony import */ var mobx_react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(mobx_react__WEBPACK_IMPORTED_MODULE_2__);



class MobxTimer {
    secondsPassed = 0;
    constructor() {
        (0,mobx__WEBPACK_IMPORTED_MODULE_1__.makeAutoObservable)(this);
    }
    reset() {
        this.secondsPassed = 0;
    }
    increaseTimer() {
        this.secondsPassed += 1;
    }
}
const mobxTimer = new MobxTimer();
setInterval(() => {
    mobxTimer.increaseTimer();
}, 1000);
const MobxTimerView = (0,mobx_react__WEBPACK_IMPORTED_MODULE_2__.observer)(({ mobxTimer }) => ((0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("button", { onClick: () => mobxTimer.reset(), children: ["Jupyter SSH Mobx: ", mobxTimer.secondsPassed] })));


/***/ }),

/***/ "./lib/tabs/AboutTab.js":
/*!******************************!*\
  !*** ./lib/tabs/AboutTab.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-runtime */ "../../../node_modules/react/jsx-runtime.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/Pagehead/Pagehead.js");
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/Label/Label.js");
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/Box/Box.js");
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/Text/Text.js");
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/Link/Link.js");
/* harmony import */ var _datalayer_icons_react_eggs_PirateSkull2Icon__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @datalayer/icons-react/eggs/PirateSkull2Icon */ "../../icons/react/eggs/esm/PirateSkull2Icon.js");




const AboutTab = (props) => {
    const { version } = props;
    const [pirate, setPirate] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(false);
    return ((0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.Fragment, { children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)(_primer_react__WEBPACK_IMPORTED_MODULE_2__["default"], { children: ["\uD83E\uDE90 \uD83D\uDCBB Jupyter SSH", (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_3__["default"], { sx: { marginLeft: 1 }, children: version })] }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_4__["default"], { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_5__["default"], { children: "Manage SSH from Jupyter." }) }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_4__["default"], { mt: 3, children: !pirate ?
                    (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("img", { src: "https://assets.datalayer.tech/releases/datalayer-0.2.0-omalley.png", onClick: e => setPirate(true) })
                    :
                        (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_datalayer_icons_react_eggs_PirateSkull2Icon__WEBPACK_IMPORTED_MODULE_6__["default"], { size: 500, onClick: e => setPirate(false) }) }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_4__["default"], { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_7__["default"], { href: "https://datalayer.tech/docs/releases/0.2.0-omalley", target: "_blank", children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_5__["default"], { as: "h4", children: "O'Malley release" }) }) }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_4__["default"], { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_7__["default"], { href: "https://github.com/datalayer/jupyter-ssh", target: "_blank", children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_5__["default"], { as: "h4", children: "Source code" }) }) })] }));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (AboutTab);


/***/ }),

/***/ "./lib/tabs/ContainersTab.js":
/*!***********************************!*\
  !*** ./lib/tabs/ContainersTab.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-runtime */ "../../../node_modules/react/jsx-runtime.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/Box/Box.js");
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/Text/Text.js");
/* harmony import */ var _primer_react_drafts__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @primer/react/drafts */ "../../../node_modules/@primer/react/lib-esm/DataTable/index.js");
/* harmony import */ var _primer_react_drafts__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @primer/react/drafts */ "../../../node_modules/@primer/react/lib-esm/DataTable/DataTable.js");
/* harmony import */ var _jupyterlab_handler__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../jupyterlab/handler */ "./lib/jupyterlab/handler.js");





const Containers = () => {
    const [containers, setContainers] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(new Array());
    (0,react__WEBPACK_IMPORTED_MODULE_1__.useEffect)(() => {
        (0,_jupyterlab_handler__WEBPACK_IMPORTED_MODULE_2__.requestAPI)('containers')
            .then(data => {
            const containers = data.containers.map((container, id) => {
                return {
                    id,
                    ...container,
                };
            });
            setContainers(containers);
        })
            .catch(reason => {
            console.error(`Error while accessing the jupyter server jupyter_ssh extension.\n${reason}`);
        });
    }, []);
    return ((0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.Fragment, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_3__["default"], { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_4__.Table.Container, { children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_4__.Table.Title, { as: "h2", id: "containers", children: "SSH containers" }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_4__.Table.Subtitle, { as: "p", id: "containers-subtitle", children: "List of SSH containers." }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_5__.DataTable, { "aria-labelledby": "containers", "aria-describedby": "containers-subtitle", data: containers, columns: [
                            {
                                header: 'Image',
                                field: 'Config.Image',
                                renderCell: row => (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_6__["default"], { children: row.Config.Image })
                            },
                            {
                                header: 'Id',
                                field: 'Id',
                                renderCell: row => (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_6__["default"], { children: row.Id })
                            },
                            {
                                header: 'Created',
                                field: 'Created',
                                renderCell: row => (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_6__["default"], { children: row.Created })
                            },
                        ] })] }) }) }));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Containers);


/***/ }),

/***/ "./lib/tabs/ImagesTab.js":
/*!*******************************!*\
  !*** ./lib/tabs/ImagesTab.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-runtime */ "../../../node_modules/react/jsx-runtime.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/Box/Box.js");
/* harmony import */ var _primer_react__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @primer/react */ "../../../node_modules/@primer/react/lib-esm/Text/Text.js");
/* harmony import */ var _primer_react_drafts__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @primer/react/drafts */ "../../../node_modules/@primer/react/lib-esm/DataTable/index.js");
/* harmony import */ var _primer_react_drafts__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @primer/react/drafts */ "../../../node_modules/@primer/react/lib-esm/DataTable/DataTable.js");
/* harmony import */ var _jupyterlab_handler__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../jupyterlab/handler */ "./lib/jupyterlab/handler.js");
/* harmony import */ var _utils_Utils__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./../utils/Utils */ "./lib/utils/Utils.js");






const Images = () => {
    const [images, setImages] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(new Array());
    (0,react__WEBPACK_IMPORTED_MODULE_1__.useEffect)(() => {
        (0,_jupyterlab_handler__WEBPACK_IMPORTED_MODULE_2__.requestAPI)('images')
            .then(data => {
            const images = data.images.map((image, id) => {
                return {
                    id,
                    ...image,
                };
            });
            setImages(images.filter(image => image.RepoTags.length > 0));
        })
            .catch(reason => {
            console.error(`Error while accessing the jupyter server jupyter_ssh extension.\n${reason}`);
        });
    }, []);
    return ((0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.Fragment, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_3__["default"], { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_4__.Table.Container, { children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_4__.Table.Title, { as: "h2", id: "images", children: "SSH images" }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_4__.Table.Subtitle, { as: "p", id: "images-subtitle", children: "List of SSH images." }), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react_drafts__WEBPACK_IMPORTED_MODULE_5__.DataTable, { "aria-labelledby": "images", "aria-describedby": "images-subtitle", data: images, columns: [
                            {
                                header: 'RepoTags',
                                field: 'RepoTags',
                                renderCell: row => (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.Fragment, { children: row.RepoTags.map(repoTag => (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_3__["default"], { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_6__["default"], { children: (0,_utils_Utils__WEBPACK_IMPORTED_MODULE_7__.strip)(repoTag, 40) }) })) })
                            },
                            {
                                header: 'Size',
                                field: 'Size',
                                renderCell: row => (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_6__["default"], { children: row.Size })
                            },
                            {
                                header: 'Os',
                                field: 'Os',
                                renderCell: row => (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_primer_react__WEBPACK_IMPORTED_MODULE_6__["default"], { children: row.Os })
                            },
                        ] })] }) }) }));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Images);


/***/ }),

/***/ "./lib/timer/TimerView.js":
/*!********************************!*\
  !*** ./lib/timer/TimerView.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TimerView": () => (/* binding */ TimerView)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-runtime */ "../../../node_modules/react/jsx-runtime.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _state__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../state */ "./lib/state/index.js");



const TimerView = () => {
    const { timer, increaseTimer, secondsPassed } = (0,_state__WEBPACK_IMPORTED_MODULE_2__["default"])();
    (0,react__WEBPACK_IMPORTED_MODULE_1__.useEffect)(() => {
        setInterval(() => {
            increaseTimer();
        }, 1000);
    }, []);
    return ((0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("button", { onClick: () => timer.reset(), children: ["Jupyter SSH: ", secondsPassed] }));
};


/***/ }),

/***/ "./lib/utils/Utils.js":
/*!****************************!*\
  !*** ./lib/utils/Utils.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "strip": () => (/* binding */ strip)
/* harmony export */ });
const strip = (s, max) => {
    if (s.length > max) {
        return s.slice(0, max) + '...';
    }
    return s;
};


/***/ }),

/***/ "./style/index.css":
/*!*************************!*\
  !*** ./style/index.css ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../../../../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "../../../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !!../../../../node_modules/css-loader/dist/cjs.js!./index.css */ "../../../node_modules/css-loader/dist/cjs.js!./style/index.css");

            

var options = {};

options.insert = "head";
options.singleton = false;

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__["default"], options);



/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__["default"].locals || {});

/***/ }),

/***/ "../../icons/react/data1/esm/LaptopSimpleIcon.svg":
/*!********************************************************!*\
  !*** ../../icons/react/data1/esm/LaptopSimpleIcon.svg ***!
  \********************************************************/
/***/ ((module) => {

module.exports = "<svg xmlns=\"http://www.w3.org/2000/svg\" class=\"icon\" viewBox=\"0 0 1024 1024\" fill=\"currentColor\" aria-hidden=\"true\">\n  <path d=\"M956.9 845.1L896.4 632V168c0-17.7-14.3-32-32-32h-704c-17.7 0-32 14.3-32 32v464L67.9 845.1C60.4 866 75.8 888 98 888h828.8c22.2 0 37.6-22 30.1-42.9zM200.4 208h624v395h-624V208zm228.3 608l8.1-37h150.3l8.1 37H428.7zm224 0l-19.1-86.7c-.8-3.7-4.1-6.3-7.8-6.3H398.2c-3.8 0-7 2.6-7.8 6.3L371.3 816H151l42.3-149h638.2l42.3 149H652.7z\"/>\n</svg>\n";

/***/ })

}]);
//# sourceMappingURL=lib_jupyterlab_index_js.b9c06fb4a0b461b948bb.js.map