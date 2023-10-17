"use strict";(self.webpackChunkjupyterlab_search_replace=self.webpackChunkjupyterlab_search_replace||[]).push([[593,418,185],{593:(e,t,o)=>{function r(e,t,o){return isNaN(e)||e<=t?t:e>=o?o:e}function a(e,t,o){return isNaN(e)||e<=t?0:e>=o?1:e/(o-t)}function i(e,t,o){return isNaN(e)?t:t+e*(o-t)}function l(e){return e*(Math.PI/180)}function n(e,t,o){return isNaN(e)||e<=0?t:e>=1?o:t+e*(o-t)}function s(e,t,o){if(e<=0)return t%360;if(e>=1)return o%360;const r=(t-o+360)%360;return r<=(o-t+360)%360?(t-r*e+360)%360:(t+r*e+360)%360}function c(e,t){const o=Math.pow(10,t);return Math.round(e*o)/o}o.r(t),o.d(t,{Accordion:()=>rr.Accordion,AccordionItem:()=>rr.AccordionItem,Anchor:()=>Zr,AnchoredRegion:()=>rr.AnchoredRegion,Avatar:()=>Qr,Badge:()=>rr.Badge,Breadcrumb:()=>rr.Breadcrumb,BreadcrumbItem:()=>rr.BreadcrumbItem,Button:()=>fa,Card:()=>va,Checkbox:()=>rr.Checkbox,Combobox:()=>Va,ContrastTarget:()=>Ko,DataGrid:()=>rr.DataGrid,DataGridCell:()=>rr.DataGridCell,DataGridRow:()=>rr.DataGridRow,DateField:()=>Ia,Dialog:()=>rr.Dialog,DirectionalStyleSheetBehavior:()=>ar,Divider:()=>rr.Divider,ListboxElement:()=>rr.ListboxElement,Menu:()=>rr.Menu,MenuItem:()=>rr.MenuItem,NumberField:()=>ei,Option:()=>rr.ListboxOption,PaletteRGB:()=>ee,Progress:()=>rr.BaseProgress,Radio:()=>rr.Radio,RadioGroup:()=>rr.RadioGroup,Search:()=>gi,Select:()=>mi,SliderLabel:()=>Ci,StandardLuminance:()=>re,SwatchRGB:()=>Y,Tab:()=>rr.Tab,TabPanel:()=>rr.TabPanel,Tabs:()=>rr.Tabs,TextArea:()=>Oi,TextField:()=>Ai,Toolbar:()=>Pi,Tooltip:()=>rr.Tooltip,accentColor:()=>vt,accentFillActive:()=>It,accentFillActiveDelta:()=>Ee,accentFillFocus:()=>Mt,accentFillFocusDelta:()=>qe,accentFillHover:()=>At,accentFillHoverDelta:()=>_e,accentFillRecipe:()=>Nt,accentFillRest:()=>Rt,accentFillRestDelta:()=>Ge,accentForegroundActive:()=>to,accentForegroundActiveDelta:()=>Xe,accentForegroundFocus:()=>oo,accentForegroundFocusDelta:()=>Ze,accentForegroundHover:()=>eo,accentForegroundHoverDelta:()=>Ue,accentForegroundRecipe:()=>Kt,accentForegroundRest:()=>Qt,accentForegroundRestDelta:()=>We,accentPalette:()=>yt,accordionItemStyles:()=>Or,accordionStyles:()=>zr,addJupyterLabThemeChangeListener:()=>qo,allComponents:()=>Qi,anchorStyles:()=>Xr,anchoredRegionStyles:()=>Jr,applyJupyterTheme:()=>Xo,avatarStyles:()=>ta,badgeStyles:()=>ra,baseErrorColor:()=>Jo,baseHeightMultiplier:()=>ge,baseHorizontalSpacingMultiplier:()=>be,baseLayerLuminance:()=>fe,black:()=>Yo,bodyFont:()=>pe,breadcrumbItemStyles:()=>na,breadcrumbStyles:()=>ia,cardStyles:()=>ma,checkboxStyles:()=>wa,comboboxStyles:()=>Ca,controlCornerRadius:()=>$e,dataGridCellStyles:()=>za,dataGridRowStyles:()=>Sa,dataGridStyles:()=>Ba,dateFieldStyles:()=>Pa,dateFieldTemplate:()=>Ga,density:()=>xe,designUnit:()=>me,dialogStyles:()=>Ea,direction:()=>ve,disabledOpacity:()=>ye,dividerStyles:()=>Wa,errorBase:()=>or,errorFillActive:()=>hr,errorFillAlgorithm:()=>Qo,errorFillFocus:()=>ur,errorFillHover:()=>dr,errorFillRecipe:()=>sr,errorFillRest:()=>cr,errorForegroundActive:()=>Vr,errorForegroundAlgorithm:()=>er,errorForegroundFocus:()=>Dr,errorForegroundHover:()=>Cr,errorForegroundRecipe:()=>Fr,errorForegroundRest:()=>Tr,errorPalette:()=>nr,fillColor:()=>Lt,focusStrokeInner:()=>So,focusStrokeInnerRecipe:()=>Do,focusStrokeOuter:()=>Vo,focusStrokeOuterRecipe:()=>Co,focusStrokeWidth:()=>ke,foregroundOnAccentActive:()=>qt,foregroundOnAccentActiveLarge:()=>Yt,foregroundOnAccentFocus:()=>Wt,foregroundOnAccentFocusLarge:()=>Jt,foregroundOnAccentHover:()=>Et,foregroundOnAccentHoverLarge:()=>Zt,foregroundOnAccentLargeRecipe:()=>Ut,foregroundOnAccentRecipe:()=>Gt,foregroundOnAccentRest:()=>_t,foregroundOnAccentRestLarge:()=>Xt,foregroundOnErrorActive:()=>$r,foregroundOnErrorActiveLarge:()=>wr,foregroundOnErrorAlgorithm:()=>tr,foregroundOnErrorFocus:()=>xr,foregroundOnErrorFocusLarge:()=>kr,foregroundOnErrorHover:()=>fr,foregroundOnErrorHoverLarge:()=>yr,foregroundOnErrorLargeRecipe:()=>mr,foregroundOnErrorRecipe:()=>gr,foregroundOnErrorRest:()=>br,foregroundOnErrorRestLarge:()=>vr,horizontalSliderLabelStyles:()=>ki,imgTemplate:()=>ea,isDark:()=>R,jpAccordion:()=>Rr,jpAccordionItem:()=>Nr,jpAnchor:()=>Yr,jpAnchoredRegion:()=>Kr,jpAvatar:()=>oa,jpBadge:()=>aa,jpBreadcrumb:()=>la,jpBreadcrumbItem:()=>sa,jpButton:()=>$a,jpCard:()=>ya,jpCheckbox:()=>ka,jpCombobox:()=>Da,jpDataGrid:()=>La,jpDataGridCell:()=>ja,jpDataGridRow:()=>Ha,jpDateField:()=>_a,jpDialog:()=>qa,jpDivider:()=>Ua,jpListbox:()=>Za,jpMenu:()=>Ja,jpMenuItem:()=>Qa,jpNumberField:()=>oi,jpOption:()=>ai,jpProgress:()=>li,jpProgressRing:()=>ni,jpRadio:()=>ci,jpRadioGroup:()=>hi,jpSearch:()=>xi,jpSelect:()=>vi,jpSlider:()=>yi,jpSliderLabel:()=>Vi,jpSwitch:()=>Di,jpTab:()=>ji,jpTabPanel:()=>Bi,jpTabs:()=>Li,jpTextArea:()=>Ri,jpTextField:()=>Mi,jpToolbar:()=>_i,jpTooltip:()=>qi,jpTreeItem:()=>Ji,jpTreeView:()=>Ki,listboxStyles:()=>Xa,menuItemStyles:()=>Ka,menuStyles:()=>Ya,neutralColor:()=>xt,neutralFillActive:()=>lo,neutralFillActiveDelta:()=>Ke,neutralFillFocus:()=>no,neutralFillFocusDelta:()=>Qe,neutralFillHover:()=>io,neutralFillHoverDelta:()=>Je,neutralFillInputActive:()=>uo,neutralFillInputActiveDelta:()=>ot,neutralFillInputFocus:()=>po,neutralFillInputFocusDelta:()=>rt,neutralFillInputHover:()=>ho,neutralFillInputHoverDelta:()=>tt,neutralFillInputRecipe:()=>so,neutralFillInputRest:()=>co,neutralFillInputRestDelta:()=>et,neutralFillLayerRecipe:()=>Fo,neutralFillLayerRest:()=>To,neutralFillLayerRestDelta:()=>ut,neutralFillRecipe:()=>ro,neutralFillRest:()=>ao,neutralFillRestDelta:()=>Ye,neutralFillStealthActive:()=>$o,neutralFillStealthActiveDelta:()=>lt,neutralFillStealthFocus:()=>xo,neutralFillStealthFocusDelta:()=>nt,neutralFillStealthHover:()=>fo,neutralFillStealthHoverDelta:()=>it,neutralFillStealthRecipe:()=>go,neutralFillStealthRest:()=>bo,neutralFillStealthRestDelta:()=>at,neutralFillStrongActive:()=>wo,neutralFillStrongActiveDelta:()=>dt,neutralFillStrongFocus:()=>ko,neutralFillStrongFocusDelta:()=>ht,neutralFillStrongHover:()=>yo,neutralFillStrongHoverDelta:()=>ct,neutralFillStrongRecipe:()=>mo,neutralFillStrongRest:()=>vo,neutralFillStrongRestDelta:()=>st,neutralForegroundHint:()=>zo,neutralForegroundHintRecipe:()=>Bo,neutralForegroundRecipe:()=>jo,neutralForegroundRest:()=>Ho,neutralLayer1:()=>Vt,neutralLayer1Recipe:()=>Ct,neutralLayer2:()=>St,neutralLayer2Recipe:()=>Dt,neutralLayer3:()=>zt,neutralLayer3Recipe:()=>Bt,neutralLayer4:()=>Ht,neutralLayer4Recipe:()=>jt,neutralLayerCardContainer:()=>kt,neutralLayerCardContainerRecipe:()=>wt,neutralLayerFloating:()=>Tt,neutralLayerFloatingRecipe:()=>Ft,neutralPalette:()=>mt,neutralStrokeActive:()=>Ro,neutralStrokeActiveDelta:()=>bt,neutralStrokeDividerRecipe:()=>Io,neutralStrokeDividerRest:()=>Mo,neutralStrokeDividerRestDelta:()=>$t,neutralStrokeFocus:()=>Ao,neutralStrokeFocusDelta:()=>ft,neutralStrokeHover:()=>No,neutralStrokeHoverDelta:()=>gt,neutralStrokeRecipe:()=>Lo,neutralStrokeRest:()=>Oo,neutralStrokeRestDelta:()=>pt,numberFieldStyles:()=>ti,optionStyles:()=>ri,progressStyles:()=>ii,provideJupyterDesignSystem:()=>Sr,radioGroupStyles:()=>di,radioStyles:()=>si,searchStyles:()=>$i,selectStyles:()=>Ta,sliderLabelStyles:()=>Ti,strokeWidth:()=>we,tabPanelStyles:()=>Si,tabStyles:()=>zi,tabsStyles:()=>Hi,textAreaStyles:()=>Ni,textFieldStyles:()=>Ii,toolbarStyles:()=>Gi,tooltipStyles:()=>Ei,typeRampBaseFontSize:()=>Fe,typeRampBaseLineHeight:()=>Te,typeRampMinus1FontSize:()=>Ce,typeRampMinus1LineHeight:()=>Ve,typeRampMinus2FontSize:()=>De,typeRampMinus2LineHeight:()=>Se,typeRampPlus1FontSize:()=>Be,typeRampPlus1LineHeight:()=>ze,typeRampPlus2FontSize:()=>je,typeRampPlus2LineHeight:()=>He,typeRampPlus3FontSize:()=>Le,typeRampPlus3LineHeight:()=>Oe,typeRampPlus4FontSize:()=>Ne,typeRampPlus4LineHeight:()=>Re,typeRampPlus5FontSize:()=>Ae,typeRampPlus5LineHeight:()=>Ie,typeRampPlus6FontSize:()=>Me,typeRampPlus6LineHeight:()=>Pe,verticalSliderLabelStyles:()=>Fi,white:()=>Zo}),Math.PI;class d{constructor(e,t,o,r){this.r=e,this.g=t,this.b=o,this.a="number"!=typeof r||isNaN(r)?1:r}static fromObject(e){return!e||isNaN(e.r)||isNaN(e.g)||isNaN(e.b)?null:new d(e.r,e.g,e.b,e.a)}equalValue(e){return this.r===e.r&&this.g===e.g&&this.b===e.b&&this.a===e.a}toStringHexRGB(){return"#"+[this.r,this.g,this.b].map(this.formatHexValue).join("")}toStringHexRGBA(){return this.toStringHexRGB()+this.formatHexValue(this.a)}toStringHexARGB(){return"#"+[this.a,this.r,this.g,this.b].map(this.formatHexValue).join("")}toStringWebRGB(){return`rgb(${Math.round(i(this.r,0,255))},${Math.round(i(this.g,0,255))},${Math.round(i(this.b,0,255))})`}toStringWebRGBA(){return`rgba(${Math.round(i(this.r,0,255))},${Math.round(i(this.g,0,255))},${Math.round(i(this.b,0,255))},${r(this.a,0,1)})`}roundToPrecision(e){return new d(c(this.r,e),c(this.g,e),c(this.b,e),c(this.a,e))}clamp(){return new d(r(this.r,0,1),r(this.g,0,1),r(this.b,0,1),r(this.a,0,1))}toObject(){return{r:this.r,g:this.g,b:this.b,a:this.a}}formatHexValue(e){return function(e){const t=Math.round(r(e,0,255)).toString(16);return 1===t.length?"0"+t:t}(i(e,0,255))}}const h={aliceblue:{r:.941176,g:.972549,b:1},antiquewhite:{r:.980392,g:.921569,b:.843137},aqua:{r:0,g:1,b:1},aquamarine:{r:.498039,g:1,b:.831373},azure:{r:.941176,g:1,b:1},beige:{r:.960784,g:.960784,b:.862745},bisque:{r:1,g:.894118,b:.768627},black:{r:0,g:0,b:0},blanchedalmond:{r:1,g:.921569,b:.803922},blue:{r:0,g:0,b:1},blueviolet:{r:.541176,g:.168627,b:.886275},brown:{r:.647059,g:.164706,b:.164706},burlywood:{r:.870588,g:.721569,b:.529412},cadetblue:{r:.372549,g:.619608,b:.627451},chartreuse:{r:.498039,g:1,b:0},chocolate:{r:.823529,g:.411765,b:.117647},coral:{r:1,g:.498039,b:.313725},cornflowerblue:{r:.392157,g:.584314,b:.929412},cornsilk:{r:1,g:.972549,b:.862745},crimson:{r:.862745,g:.078431,b:.235294},cyan:{r:0,g:1,b:1},darkblue:{r:0,g:0,b:.545098},darkcyan:{r:0,g:.545098,b:.545098},darkgoldenrod:{r:.721569,g:.52549,b:.043137},darkgray:{r:.662745,g:.662745,b:.662745},darkgreen:{r:0,g:.392157,b:0},darkgrey:{r:.662745,g:.662745,b:.662745},darkkhaki:{r:.741176,g:.717647,b:.419608},darkmagenta:{r:.545098,g:0,b:.545098},darkolivegreen:{r:.333333,g:.419608,b:.184314},darkorange:{r:1,g:.54902,b:0},darkorchid:{r:.6,g:.196078,b:.8},darkred:{r:.545098,g:0,b:0},darksalmon:{r:.913725,g:.588235,b:.478431},darkseagreen:{r:.560784,g:.737255,b:.560784},darkslateblue:{r:.282353,g:.239216,b:.545098},darkslategray:{r:.184314,g:.309804,b:.309804},darkslategrey:{r:.184314,g:.309804,b:.309804},darkturquoise:{r:0,g:.807843,b:.819608},darkviolet:{r:.580392,g:0,b:.827451},deeppink:{r:1,g:.078431,b:.576471},deepskyblue:{r:0,g:.74902,b:1},dimgray:{r:.411765,g:.411765,b:.411765},dimgrey:{r:.411765,g:.411765,b:.411765},dodgerblue:{r:.117647,g:.564706,b:1},firebrick:{r:.698039,g:.133333,b:.133333},floralwhite:{r:1,g:.980392,b:.941176},forestgreen:{r:.133333,g:.545098,b:.133333},fuchsia:{r:1,g:0,b:1},gainsboro:{r:.862745,g:.862745,b:.862745},ghostwhite:{r:.972549,g:.972549,b:1},gold:{r:1,g:.843137,b:0},goldenrod:{r:.854902,g:.647059,b:.12549},gray:{r:.501961,g:.501961,b:.501961},green:{r:0,g:.501961,b:0},greenyellow:{r:.678431,g:1,b:.184314},grey:{r:.501961,g:.501961,b:.501961},honeydew:{r:.941176,g:1,b:.941176},hotpink:{r:1,g:.411765,b:.705882},indianred:{r:.803922,g:.360784,b:.360784},indigo:{r:.294118,g:0,b:.509804},ivory:{r:1,g:1,b:.941176},khaki:{r:.941176,g:.901961,b:.54902},lavender:{r:.901961,g:.901961,b:.980392},lavenderblush:{r:1,g:.941176,b:.960784},lawngreen:{r:.486275,g:.988235,b:0},lemonchiffon:{r:1,g:.980392,b:.803922},lightblue:{r:.678431,g:.847059,b:.901961},lightcoral:{r:.941176,g:.501961,b:.501961},lightcyan:{r:.878431,g:1,b:1},lightgoldenrodyellow:{r:.980392,g:.980392,b:.823529},lightgray:{r:.827451,g:.827451,b:.827451},lightgreen:{r:.564706,g:.933333,b:.564706},lightgrey:{r:.827451,g:.827451,b:.827451},lightpink:{r:1,g:.713725,b:.756863},lightsalmon:{r:1,g:.627451,b:.478431},lightseagreen:{r:.12549,g:.698039,b:.666667},lightskyblue:{r:.529412,g:.807843,b:.980392},lightslategray:{r:.466667,g:.533333,b:.6},lightslategrey:{r:.466667,g:.533333,b:.6},lightsteelblue:{r:.690196,g:.768627,b:.870588},lightyellow:{r:1,g:1,b:.878431},lime:{r:0,g:1,b:0},limegreen:{r:.196078,g:.803922,b:.196078},linen:{r:.980392,g:.941176,b:.901961},magenta:{r:1,g:0,b:1},maroon:{r:.501961,g:0,b:0},mediumaquamarine:{r:.4,g:.803922,b:.666667},mediumblue:{r:0,g:0,b:.803922},mediumorchid:{r:.729412,g:.333333,b:.827451},mediumpurple:{r:.576471,g:.439216,b:.858824},mediumseagreen:{r:.235294,g:.701961,b:.443137},mediumslateblue:{r:.482353,g:.407843,b:.933333},mediumspringgreen:{r:0,g:.980392,b:.603922},mediumturquoise:{r:.282353,g:.819608,b:.8},mediumvioletred:{r:.780392,g:.082353,b:.521569},midnightblue:{r:.098039,g:.098039,b:.439216},mintcream:{r:.960784,g:1,b:.980392},mistyrose:{r:1,g:.894118,b:.882353},moccasin:{r:1,g:.894118,b:.709804},navajowhite:{r:1,g:.870588,b:.678431},navy:{r:0,g:0,b:.501961},oldlace:{r:.992157,g:.960784,b:.901961},olive:{r:.501961,g:.501961,b:0},olivedrab:{r:.419608,g:.556863,b:.137255},orange:{r:1,g:.647059,b:0},orangered:{r:1,g:.270588,b:0},orchid:{r:.854902,g:.439216,b:.839216},palegoldenrod:{r:.933333,g:.909804,b:.666667},palegreen:{r:.596078,g:.984314,b:.596078},paleturquoise:{r:.686275,g:.933333,b:.933333},palevioletred:{r:.858824,g:.439216,b:.576471},papayawhip:{r:1,g:.937255,b:.835294},peachpuff:{r:1,g:.854902,b:.72549},peru:{r:.803922,g:.521569,b:.247059},pink:{r:1,g:.752941,b:.796078},plum:{r:.866667,g:.627451,b:.866667},powderblue:{r:.690196,g:.878431,b:.901961},purple:{r:.501961,g:0,b:.501961},red:{r:1,g:0,b:0},rosybrown:{r:.737255,g:.560784,b:.560784},royalblue:{r:.254902,g:.411765,b:.882353},saddlebrown:{r:.545098,g:.270588,b:.07451},salmon:{r:.980392,g:.501961,b:.447059},sandybrown:{r:.956863,g:.643137,b:.376471},seagreen:{r:.180392,g:.545098,b:.341176},seashell:{r:1,g:.960784,b:.933333},sienna:{r:.627451,g:.321569,b:.176471},silver:{r:.752941,g:.752941,b:.752941},skyblue:{r:.529412,g:.807843,b:.921569},slateblue:{r:.415686,g:.352941,b:.803922},slategray:{r:.439216,g:.501961,b:.564706},slategrey:{r:.439216,g:.501961,b:.564706},snow:{r:1,g:.980392,b:.980392},springgreen:{r:0,g:1,b:.498039},steelblue:{r:.27451,g:.509804,b:.705882},tan:{r:.823529,g:.705882,b:.54902},teal:{r:0,g:.501961,b:.501961},thistle:{r:.847059,g:.74902,b:.847059},tomato:{r:1,g:.388235,b:.278431},transparent:{r:0,g:0,b:0,a:0},turquoise:{r:.25098,g:.878431,b:.815686},violet:{r:.933333,g:.509804,b:.933333},wheat:{r:.960784,g:.870588,b:.701961},white:{r:1,g:1,b:1},whitesmoke:{r:.960784,g:.960784,b:.960784},yellow:{r:1,g:1,b:0},yellowgreen:{r:.603922,g:.803922,b:.196078}},u=/^rgb\(\s*((?:(?:25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\s*,\s*){2}(?:25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\s*)\)$/i,p=/^rgba\(\s*((?:(?:25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\s*,\s*){3}(?:0|1|0?\.\d*)\s*)\)$/i,g=/^#((?:[0-9a-f]{6}|[0-9a-f]{3}))$/i,b=/^#((?:[0-9a-f]{8}|[0-9a-f]{4}))$/i;function f(e){const t=g.exec(e);if(null===t)return null;let o=t[1];if(3===o.length){const e=o.charAt(0),t=o.charAt(1),r=o.charAt(2);o=e.concat(e,t,t,r,r)}const r=parseInt(o,16);return isNaN(r)?null:new d(a((16711680&r)>>>16,0,255),a((65280&r)>>>8,0,255),a(255&r,0,255),1)}function $(e){const t=e.toLowerCase();return function(e){return g.test(e)}(t)?f(t):function(e){return function(e){return b.test(e)}(e)}(t)?function(e){const t=b.exec(e);if(null===t)return null;let o=t[1];if(4===o.length){const e=o.charAt(0),t=o.charAt(1),r=o.charAt(2),a=o.charAt(3);o=e.concat(e,t,t,r,r,a,a)}const r=parseInt(o,16);return isNaN(r)?null:new d(a((16711680&r)>>>16,0,255),a((65280&r)>>>8,0,255),a(255&r,0,255),a((4278190080&r)>>>24,0,255))}(t):function(e){return u.test(e)}(t)?function(e){const t=u.exec(e);if(null===t)return null;const o=t[1].split(",");return new d(a(Number(o[0]),0,255),a(Number(o[1]),0,255),a(Number(o[2]),0,255),1)}(t):function(e){return p.test(e)}(t)?function(e){const t=p.exec(e);if(null===t)return null;const o=t[1].split(",");return 4===o.length?new d(a(Number(o[0]),0,255),a(Number(o[1]),0,255),a(Number(o[2]),0,255),Number(o[3])):null}(t):function(e){return h.hasOwnProperty(e)}(t)?function(e){const t=h[e.toLowerCase()];return t?new d(t.r,t.g,t.b,t.hasOwnProperty("a")?t.a:void 0):null}(t):null}class x{constructor(e,t,o){this.h=e,this.s=t,this.l=o}static fromObject(e){return!e||isNaN(e.h)||isNaN(e.s)||isNaN(e.l)?null:new x(e.h,e.s,e.l)}equalValue(e){return this.h===e.h&&this.s===e.s&&this.l===e.l}roundToPrecision(e){return new x(c(this.h,e),c(this.s,e),c(this.l,e))}toObject(){return{h:this.h,s:this.s,l:this.l}}}class m{constructor(e,t,o){this.h=e,this.s=t,this.v=o}static fromObject(e){return!e||isNaN(e.h)||isNaN(e.s)||isNaN(e.v)?null:new m(e.h,e.s,e.v)}equalValue(e){return this.h===e.h&&this.s===e.s&&this.v===e.v}roundToPrecision(e){return new m(c(this.h,e),c(this.s,e),c(this.v,e))}toObject(){return{h:this.h,s:this.s,v:this.v}}}class v{constructor(e,t,o){this.l=e,this.a=t,this.b=o}static fromObject(e){return!e||isNaN(e.l)||isNaN(e.a)||isNaN(e.b)?null:new v(e.l,e.a,e.b)}equalValue(e){return this.l===e.l&&this.a===e.a&&this.b===e.b}roundToPrecision(e){return new v(c(this.l,e),c(this.a,e),c(this.b,e))}toObject(){return{l:this.l,a:this.a,b:this.b}}}v.epsilon=216/24389,v.kappa=24389/27;class y{constructor(e,t,o){this.l=e,this.c=t,this.h=o}static fromObject(e){return!e||isNaN(e.l)||isNaN(e.c)||isNaN(e.h)?null:new y(e.l,e.c,e.h)}equalValue(e){return this.l===e.l&&this.c===e.c&&this.h===e.h}roundToPrecision(e){return new y(c(this.l,e),c(this.c,e),c(this.h,e))}toObject(){return{l:this.l,c:this.c,h:this.h}}}class w{constructor(e,t,o){this.x=e,this.y=t,this.z=o}static fromObject(e){return!e||isNaN(e.x)||isNaN(e.y)||isNaN(e.z)?null:new w(e.x,e.y,e.z)}equalValue(e){return this.x===e.x&&this.y===e.y&&this.z===e.z}roundToPrecision(e){return new w(c(this.x,e),c(this.y,e),c(this.z,e))}toObject(){return{x:this.x,y:this.y,z:this.z}}}function k(e){return.2126*e.r+.7152*e.g+.0722*e.b}function F(e){function t(e){return e<=.03928?e/12.92:Math.pow((e+.055)/1.055,2.4)}return k(new d(t(e.r),t(e.g),t(e.b),1))}w.whitePoint=new w(.95047,1,1.08883);const T=(e,t)=>(e+.05)/(t+.05);function C(e,t){const o=F(e),r=F(t);return o>r?T(o,r):T(r,o)}function V(e){const t=Math.max(e.r,e.g,e.b),o=Math.min(e.r,e.g,e.b),r=t-o;let a=0;0!==r&&(a=t===e.r?(e.g-e.b)/r%6*60:t===e.g?60*((e.b-e.r)/r+2):60*((e.r-e.g)/r+4)),a<0&&(a+=360);const i=(t+o)/2;let l=0;return 0!==r&&(l=r/(1-Math.abs(2*i-1))),new x(a,l,i)}function D(e,t=1){const o=(1-Math.abs(2*e.l-1))*e.s,r=o*(1-Math.abs(e.h/60%2-1)),a=e.l-o/2;let i=0,l=0,n=0;return e.h<60?(i=o,l=r,n=0):e.h<120?(i=r,l=o,n=0):e.h<180?(i=0,l=o,n=r):e.h<240?(i=0,l=r,n=o):e.h<300?(i=r,l=0,n=o):e.h<360&&(i=o,l=0,n=r),new d(i+a,l+a,n+a,t)}function S(e){const t=Math.max(e.r,e.g,e.b),o=t-Math.min(e.r,e.g,e.b);let r=0;0!==o&&(r=t===e.r?(e.g-e.b)/o%6*60:t===e.g?60*((e.b-e.r)/o+2):60*((e.r-e.g)/o+4)),r<0&&(r+=360);let a=0;return 0!==t&&(a=o/t),new m(r,a,t)}function B(e){function t(e){return e<=.04045?e/12.92:Math.pow((e+.055)/1.055,2.4)}const o=t(e.r),r=t(e.g),a=t(e.b);return new w(.4124564*o+.3575761*r+.1804375*a,.2126729*o+.7151522*r+.072175*a,.0193339*o+.119192*r+.9503041*a)}function z(e,t=1){function o(e){return e<=.0031308?12.92*e:1.055*Math.pow(e,1/2.4)-.055}const r=o(3.2404542*e.x-1.5371385*e.y-.4985314*e.z),a=o(-.969266*e.x+1.8760108*e.y+.041556*e.z),i=o(.0556434*e.x-.2040259*e.y+1.0572252*e.z);return new d(r,a,i,t)}function j(e){return function(e){function t(e){return e>v.epsilon?Math.pow(e,1/3):(v.kappa*e+16)/116}const o=t(e.x/w.whitePoint.x),r=t(e.y/w.whitePoint.y),a=t(e.z/w.whitePoint.z);return new v(116*r-16,500*(o-r),200*(r-a))}(B(e))}function H(e,t=1){return z(function(e){const t=(e.l+16)/116,o=t+e.a/500,r=t-e.b/200,a=Math.pow(o,3),i=Math.pow(t,3),l=Math.pow(r,3);let n=0;n=a>v.epsilon?a:(116*o-16)/v.kappa;let s=0;s=e.l>v.epsilon*v.kappa?i:e.l/v.kappa;let c=0;return c=l>v.epsilon?l:(116*r-16)/v.kappa,n=w.whitePoint.x*n,s=w.whitePoint.y*s,c=w.whitePoint.z*c,new w(n,s,c)}(e),t)}function L(e){return function(e){let t=0;(Math.abs(e.b)>.001||Math.abs(e.a)>.001)&&(t=Math.atan2(e.b,e.a)*(180/Math.PI)),t<0&&(t+=360);const o=Math.sqrt(e.a*e.a+e.b*e.b);return new y(e.l,o,t)}(j(e))}function O(e,t=1){return H(function(e){let t=0,o=0;return 0!==e.h&&(t=Math.cos(l(e.h))*e.c,o=Math.sin(l(e.h))*e.c),new v(e.l,t,o)}(e),t)}const N=(-.1+Math.sqrt(.21))/2;function R(e){return e.relativeLuminance<=N}function A(e,t,o=18){const r=L(e);let a=r.c+t*o;return a<0&&(a=0),O(new y(r.l,a,r.h))}function I(e,t){return e*t}function M(e,t){return new d(I(e.r,t.r),I(e.g,t.g),I(e.b,t.b),1)}function P(e,t){return r(e<.5?2*t*e:1-2*(1-t)*(1-e),0,1)}function G(e,t){return new d(P(e.r,t.r),P(e.g,t.g),P(e.b,t.b),1)}var _,E;function q(e,t,o,r){if(isNaN(e)||e<=0)return o;if(e>=1)return r;switch(t){case E.HSL:return D(function(e,t,o){return isNaN(e)||e<=0?t:e>=1?o:new x(s(e,t.h,o.h),n(e,t.s,o.s),n(e,t.l,o.l))}(e,V(o),V(r)));case E.HSV:return function(e,t=1){const o=e.s*e.v,r=o*(1-Math.abs(e.h/60%2-1)),a=e.v-o;let i=0,l=0,n=0;return e.h<60?(i=o,l=r,n=0):e.h<120?(i=r,l=o,n=0):e.h<180?(i=0,l=o,n=r):e.h<240?(i=0,l=r,n=o):e.h<300?(i=r,l=0,n=o):e.h<360&&(i=o,l=0,n=r),new d(i+a,l+a,n+a,t)}(function(e,t,o){return isNaN(e)||e<=0?t:e>=1?o:new m(s(e,t.h,o.h),n(e,t.s,o.s),n(e,t.v,o.v))}(e,S(o),S(r)));case E.XYZ:return z(function(e,t,o){return isNaN(e)||e<=0?t:e>=1?o:new w(n(e,t.x,o.x),n(e,t.y,o.y),n(e,t.z,o.z))}(e,B(o),B(r)));case E.LAB:return H(function(e,t,o){return isNaN(e)||e<=0?t:e>=1?o:new v(n(e,t.l,o.l),n(e,t.a,o.a),n(e,t.b,o.b))}(e,j(o),j(r)));case E.LCH:return O(function(e,t,o){return isNaN(e)||e<=0?t:e>=1?o:new y(n(e,t.l,o.l),n(e,t.c,o.c),s(e,t.h,o.h))}(e,L(o),L(r)));default:return function(e,t,o){return isNaN(e)||e<=0?t:e>=1?o:new d(n(e,t.r,o.r),n(e,t.g,o.g),n(e,t.b,o.b),n(e,t.a,o.a))}(e,o,r)}}!function(e){e[e.Burn=0]="Burn",e[e.Color=1]="Color",e[e.Darken=2]="Darken",e[e.Dodge=3]="Dodge",e[e.Lighten=4]="Lighten",e[e.Multiply=5]="Multiply",e[e.Overlay=6]="Overlay",e[e.Screen=7]="Screen"}(_||(_={})),function(e){e[e.RGB=0]="RGB",e[e.HSL=1]="HSL",e[e.HSV=2]="HSV",e[e.XYZ=3]="XYZ",e[e.LAB=4]="LAB",e[e.LCH=5]="LCH"}(E||(E={}));class W{constructor(e){if(null==e||0===e.length)throw new Error("The stops argument must be non-empty");this.stops=this.sortColorScaleStops(e)}static createBalancedColorScale(e){if(null==e||0===e.length)throw new Error("The colors argument must be non-empty");const t=new Array(e.length);for(let o=0;o<e.length;o++)0===o?t[o]={color:e[o],position:0}:o===e.length-1?t[o]={color:e[o],position:1}:t[o]={color:e[o],position:o*(1/(e.length-1))};return new W(t)}getColor(e,t=E.RGB){if(1===this.stops.length)return this.stops[0].color;if(e<=0)return this.stops[0].color;if(e>=1)return this.stops[this.stops.length-1].color;let o=0;for(let t=0;t<this.stops.length;t++)this.stops[t].position<=e&&(o=t);let r=o+1;return r>=this.stops.length&&(r=this.stops.length-1),q((e-this.stops[o].position)*(1/(this.stops[r].position-this.stops[o].position)),t,this.stops[o].color,this.stops[r].color)}trim(e,t,o=E.RGB){if(e<0||t>1||t<e)throw new Error("Invalid bounds");if(e===t)return new W([{color:this.getColor(e,o),position:0}]);const r=[];for(let o=0;o<this.stops.length;o++)this.stops[o].position>=e&&this.stops[o].position<=t&&r.push(this.stops[o]);if(0===r.length)return new W([{color:this.getColor(e),position:e},{color:this.getColor(t),position:t}]);r[0].position!==e&&r.unshift({color:this.getColor(e),position:e}),r[r.length-1].position!==t&&r.push({color:this.getColor(t),position:t});const a=t-e,i=new Array(r.length);for(let t=0;t<r.length;t++)i[t]={color:r[t].color,position:(r[t].position-e)/a};return new W(i)}findNextColor(e,t,o=!1,r=E.RGB,a=.005,i=32){isNaN(e)||e<=0?e=0:e>=1&&(e=1);const l=this.getColor(e,r),n=o?0:1;if(C(l,this.getColor(n,r))<=t)return n;let s=o?0:e,c=o?e:0,d=n,h=0;for(;h<=i;){d=Math.abs(c-s)/2+s;const e=C(l,this.getColor(d,r));if(Math.abs(e-t)<=a)return d;e>t?o?s=d:c=d:o?c=d:s=d,h++}return d}clone(){const e=new Array(this.stops.length);for(let t=0;t<e.length;t++)e[t]={color:this.stops[t].color,position:this.stops[t].position};return new W(e)}sortColorScaleStops(e){return e.sort(((e,t)=>{const o=e.position,r=t.position;return o<r?-1:o>r?1:0}))}}class U{constructor(e){this.config=Object.assign({},U.defaultPaletteConfig,e),this.palette=[],this.updatePaletteColors()}updatePaletteGenerationValues(e){let t=!1;for(const o in e)this.config[o]&&(this.config[o].equalValue?this.config[o].equalValue(e[o])||(this.config[o]=e[o],t=!0):e[o]!==this.config[o]&&(this.config[o]=e[o],t=!0));return t&&this.updatePaletteColors(),t}updatePaletteColors(){const e=this.generatePaletteColorScale();for(let t=0;t<this.config.steps;t++)this.palette[t]=e.getColor(t/(this.config.steps-1),this.config.interpolationMode)}generatePaletteColorScale(){const e=V(this.config.baseColor),t=new W([{position:0,color:this.config.scaleColorLight},{position:.5,color:this.config.baseColor},{position:1,color:this.config.scaleColorDark}]).trim(this.config.clipLight,1-this.config.clipDark);let o=t.getColor(0),r=t.getColor(1);if(e.s>=this.config.saturationAdjustmentCutoff&&(o=A(o,this.config.saturationLight),r=A(r,this.config.saturationDark)),0!==this.config.multiplyLight){const e=M(this.config.baseColor,o);o=q(this.config.multiplyLight,this.config.interpolationMode,o,e)}if(0!==this.config.multiplyDark){const e=M(this.config.baseColor,r);r=q(this.config.multiplyDark,this.config.interpolationMode,r,e)}if(0!==this.config.overlayLight){const e=G(this.config.baseColor,o);o=q(this.config.overlayLight,this.config.interpolationMode,o,e)}if(0!==this.config.overlayDark){const e=G(this.config.baseColor,r);r=q(this.config.overlayDark,this.config.interpolationMode,r,e)}return this.config.baseScalePosition?this.config.baseScalePosition<=0?new W([{position:0,color:this.config.baseColor},{position:1,color:r.clamp()}]):this.config.baseScalePosition>=1?new W([{position:0,color:o.clamp()},{position:1,color:this.config.baseColor}]):new W([{position:0,color:o.clamp()},{position:this.config.baseScalePosition,color:this.config.baseColor},{position:1,color:r.clamp()}]):new W([{position:0,color:o.clamp()},{position:.5,color:this.config.baseColor},{position:1,color:r.clamp()}])}}U.defaultPaletteConfig={baseColor:f("#808080"),steps:11,interpolationMode:E.RGB,scaleColorLight:new d(1,1,1,1),scaleColorDark:new d(0,0,0,1),clipLight:.185,clipDark:.16,saturationAdjustmentCutoff:.05,saturationLight:.35,saturationDark:1.25,overlayLight:0,overlayDark:.25,multiplyLight:0,multiplyDark:0,baseScalePosition:.5},U.greyscalePaletteConfig={baseColor:f("#808080"),steps:11,interpolationMode:E.RGB,scaleColorLight:new d(1,1,1,1),scaleColorDark:new d(0,0,0,1),clipLight:0,clipDark:0,saturationAdjustmentCutoff:0,saturationLight:0,saturationDark:0,overlayLight:0,overlayDark:0,multiplyLight:0,multiplyDark:0,baseScalePosition:.5},U.defaultPaletteConfig.scaleColorLight,U.defaultPaletteConfig.scaleColorDark;class X{constructor(e){this.palette=[],this.config=Object.assign({},X.defaultPaletteConfig,e),this.regenPalettes()}regenPalettes(){let e=this.config.steps;(isNaN(e)||e<3)&&(e=3);const t=.14,o=new d(t,t,t,1),r=new U(Object.assign(Object.assign({},U.greyscalePaletteConfig),{baseColor:o,baseScalePosition:86/94,steps:e})).palette,a=(k(this.config.baseColor)+V(this.config.baseColor).l)/2,i=this.matchRelativeLuminanceIndex(a,r)/(e-1),l=this.matchRelativeLuminanceIndex(t,r)/(e-1),n=V(this.config.baseColor),s=D(x.fromObject({h:n.h,s:n.s,l:t})),c=D(x.fromObject({h:n.h,s:n.s,l:.06})),h=new Array(5);h[0]={position:0,color:new d(1,1,1,1)},h[1]={position:i,color:this.config.baseColor},h[2]={position:l,color:s},h[3]={position:.99,color:c},h[4]={position:1,color:new d(0,0,0,1)};const u=new W(h);this.palette=new Array(e);for(let t=0;t<e;t++){const o=u.getColor(t/(e-1),E.RGB);this.palette[t]=o}}matchRelativeLuminanceIndex(e,t){let o=Number.MAX_VALUE,r=0,a=0;const i=t.length;for(;a<i;a++){const i=Math.abs(k(t[a])-e);i<o&&(o=i,r=a)}return r}}function Z(e,t){const o=e.relativeLuminance>t.relativeLuminance?e:t,r=e.relativeLuminance>t.relativeLuminance?t:e;return(o.relativeLuminance+.05)/(r.relativeLuminance+.05)}X.defaultPaletteConfig={baseColor:f("#808080"),steps:94};const Y=Object.freeze({create:(e,t,o)=>new J(e,t,o),from:e=>new J(e.r,e.g,e.b)});class J extends d{constructor(e,t,o){super(e,t,o,1),this.toColorString=this.toStringHexRGB,this.contrast=Z.bind(null,this),this.createCSS=this.toColorString,this.relativeLuminance=F(this)}static fromObject(e){return new J(e.r,e.g,e.b)}}function K(e,t,o=0,r=e.length-1){if(r===o)return e[o];const a=Math.floor((r-o)/2)+o;return t(e[a])?K(e,t,o,a):K(e,t,a+1,r)}function Q(e){return R(e)?-1:1}const ee=Object.freeze({create:function(e,t,o){return"number"==typeof e?ee.from(Y.create(e,t,o)):ee.from(e)},from:function(e){return function(e){const t={r:0,g:0,b:0,toColorString:()=>"",contrast:()=>0,relativeLuminance:0};for(const o in t)if(typeof t[o]!=typeof e[o])return!1;return!0}(e)?te.from(e):te.from(Y.create(e.r,e.g,e.b))}});class te{constructor(e,t){this.closestIndexCache=new Map,this.source=e,this.swatches=t,this.reversedSwatches=Object.freeze([...this.swatches].reverse()),this.lastIndex=this.swatches.length-1}colorContrast(e,t,o,r){void 0===o&&(o=this.closestIndexOf(e));let a=this.swatches;const i=this.lastIndex;let l=o;return void 0===r&&(r=Q(e)),-1===r&&(a=this.reversedSwatches,l=i-l),K(a,(o=>Z(e,o)>=t),l,i)}get(e){return this.swatches[e]||this.swatches[r(e,0,this.lastIndex)]}closestIndexOf(e){if(this.closestIndexCache.has(e.relativeLuminance))return this.closestIndexCache.get(e.relativeLuminance);let t=this.swatches.indexOf(e);if(-1!==t)return this.closestIndexCache.set(e.relativeLuminance,t),t;const o=this.swatches.reduce(((t,o)=>Math.abs(o.relativeLuminance-e.relativeLuminance)<Math.abs(t.relativeLuminance-e.relativeLuminance)?o:t));return t=this.swatches.indexOf(o),this.closestIndexCache.set(e.relativeLuminance,t),t}static from(e){return new te(e,Object.freeze(new X({baseColor:d.fromObject(e)}).palette.map((e=>{const t=f(e.toStringHexRGB());return Y.create(t.r,t.g,t.b)}))))}}function oe(e){return Y.create(e,e,e)}const re={LightMode:1,DarkMode:.23};var ae=o(624),ie=o(586);const le=Y.create(1,1,1),ne=Y.create(0,0,0),se=Y.from(f("#808080")),ce=Y.from(f("#DA1A5F"));function de(e,t,o,r,a,i){return Math.max(e.closestIndexOf(oe(t))+o,r,a,i)}const{create:he}=ae.DesignToken;function ue(e){return ae.DesignToken.create({name:e,cssCustomPropertyName:null})}const pe=he("body-font").withDefault('aktiv-grotesk, "Segoe UI", Arial, Helvetica, sans-serif'),ge=he("base-height-multiplier").withDefault(10),be=he("base-horizontal-spacing-multiplier").withDefault(3),fe=he("base-layer-luminance").withDefault(re.DarkMode),$e=he("control-corner-radius").withDefault(4),xe=he("density").withDefault(0),me=he("design-unit").withDefault(4),ve=he("direction").withDefault(ie.N.ltr),ye=he("disabled-opacity").withDefault(.3),we=he("stroke-width").withDefault(1),ke=he("focus-stroke-width").withDefault(2),Fe=he("type-ramp-base-font-size").withDefault("14px"),Te=he("type-ramp-base-line-height").withDefault("20px"),Ce=he("type-ramp-minus-1-font-size").withDefault("12px"),Ve=he("type-ramp-minus-1-line-height").withDefault("16px"),De=he("type-ramp-minus-2-font-size").withDefault("10px"),Se=he("type-ramp-minus-2-line-height").withDefault("16px"),Be=he("type-ramp-plus-1-font-size").withDefault("16px"),ze=he("type-ramp-plus-1-line-height").withDefault("24px"),je=he("type-ramp-plus-2-font-size").withDefault("20px"),He=he("type-ramp-plus-2-line-height").withDefault("28px"),Le=he("type-ramp-plus-3-font-size").withDefault("28px"),Oe=he("type-ramp-plus-3-line-height").withDefault("36px"),Ne=he("type-ramp-plus-4-font-size").withDefault("34px"),Re=he("type-ramp-plus-4-line-height").withDefault("44px"),Ae=he("type-ramp-plus-5-font-size").withDefault("46px"),Ie=he("type-ramp-plus-5-line-height").withDefault("56px"),Me=he("type-ramp-plus-6-font-size").withDefault("60px"),Pe=he("type-ramp-plus-6-line-height").withDefault("72px"),Ge=ue("accent-fill-rest-delta").withDefault(0),_e=ue("accent-fill-hover-delta").withDefault(4),Ee=ue("accent-fill-active-delta").withDefault(-5),qe=ue("accent-fill-focus-delta").withDefault(0),We=ue("accent-foreground-rest-delta").withDefault(0),Ue=ue("accent-foreground-hover-delta").withDefault(6),Xe=ue("accent-foreground-active-delta").withDefault(-4),Ze=ue("accent-foreground-focus-delta").withDefault(0),Ye=ue("neutral-fill-rest-delta").withDefault(7),Je=ue("neutral-fill-hover-delta").withDefault(10),Ke=ue("neutral-fill-active-delta").withDefault(5),Qe=ue("neutral-fill-focus-delta").withDefault(0),et=ue("neutral-fill-input-rest-delta").withDefault(0),tt=ue("neutral-fill-input-hover-delta").withDefault(0),ot=ue("neutral-fill-input-active-delta").withDefault(0),rt=ue("neutral-fill-input-focus-delta").withDefault(0),at=ue("neutral-fill-stealth-rest-delta").withDefault(0),it=ue("neutral-fill-stealth-hover-delta").withDefault(5),lt=ue("neutral-fill-stealth-active-delta").withDefault(3),nt=ue("neutral-fill-stealth-focus-delta").withDefault(0),st=ue("neutral-fill-strong-rest-delta").withDefault(0),ct=ue("neutral-fill-strong-hover-delta").withDefault(8),dt=ue("neutral-fill-strong-active-delta").withDefault(-5),ht=ue("neutral-fill-strong-focus-delta").withDefault(0),ut=ue("neutral-fill-layer-rest-delta").withDefault(3),pt=ue("neutral-stroke-rest-delta").withDefault(25),gt=ue("neutral-stroke-hover-delta").withDefault(40),bt=ue("neutral-stroke-active-delta").withDefault(16),ft=ue("neutral-stroke-focus-delta").withDefault(25),$t=ue("neutral-stroke-divider-rest-delta").withDefault(8),xt=he("neutral-color").withDefault(se),mt=ue("neutral-palette").withDefault((e=>ee.from(xt.getValueFor(e)))),vt=he("accent-color").withDefault(ce),yt=ue("accent-palette").withDefault((e=>ee.from(vt.getValueFor(e)))),wt=ue("neutral-layer-card-container-recipe").withDefault({evaluate:e=>{return t=mt.getValueFor(e),o=fe.getValueFor(e),r=ut.getValueFor(e),t.get(t.closestIndexOf(oe(o))+r);var t,o,r}}),kt=he("neutral-layer-card-container").withDefault((e=>wt.getValueFor(e).evaluate(e))),Ft=ue("neutral-layer-floating-recipe").withDefault({evaluate:e=>function(e,t,o){const r=e.closestIndexOf(oe(t))-o;return e.get(r-o)}(mt.getValueFor(e),fe.getValueFor(e),ut.getValueFor(e))}),Tt=he("neutral-layer-floating").withDefault((e=>Ft.getValueFor(e).evaluate(e))),Ct=ue("neutral-layer-1-recipe").withDefault({evaluate:e=>function(e,t){return e.get(e.closestIndexOf(oe(t)))}(mt.getValueFor(e),fe.getValueFor(e))}),Vt=he("neutral-layer-1").withDefault((e=>Ct.getValueFor(e).evaluate(e))),Dt=ue("neutral-layer-2-recipe").withDefault({evaluate:e=>{return t=mt.getValueFor(e),o=fe.getValueFor(e),r=ut.getValueFor(e),a=Ye.getValueFor(e),i=Je.getValueFor(e),l=Ke.getValueFor(e),t.get(de(t,o,r,a,i,l));var t,o,r,a,i,l}}),St=he("neutral-layer-2").withDefault((e=>Dt.getValueFor(e).evaluate(e))),Bt=ue("neutral-layer-3-recipe").withDefault({evaluate:e=>{return t=mt.getValueFor(e),o=fe.getValueFor(e),r=ut.getValueFor(e),a=Ye.getValueFor(e),i=Je.getValueFor(e),l=Ke.getValueFor(e),t.get(de(t,o,r,a,i,l)+r);var t,o,r,a,i,l}}),zt=he("neutral-layer-3").withDefault((e=>Bt.getValueFor(e).evaluate(e))),jt=ue("neutral-layer-4-recipe").withDefault({evaluate:e=>{return t=mt.getValueFor(e),o=fe.getValueFor(e),r=ut.getValueFor(e),a=Ye.getValueFor(e),i=Je.getValueFor(e),l=Ke.getValueFor(e),t.get(de(t,o,r,a,i,l)+2*r);var t,o,r,a,i,l}}),Ht=he("neutral-layer-4").withDefault((e=>jt.getValueFor(e).evaluate(e))),Lt=he("fill-color").withDefault((e=>Vt.getValueFor(e)));var Ot;!function(e){e[e.normal=4.5]="normal",e[e.large=7]="large"}(Ot||(Ot={}));const Nt=he({name:"accent-fill-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>function(e,t,o,r,a,i,l,n,s){const c=e.source,d=t.closestIndexOf(o)>=Math.max(l,n,s)?-1:1,h=e.closestIndexOf(c),u=h+-1*d*r,p=u+d*a,g=u+d*i;return{rest:e.get(u),hover:e.get(h),active:e.get(p),focus:e.get(g)}}(yt.getValueFor(e),mt.getValueFor(e),t||Lt.getValueFor(e),_e.getValueFor(e),Ee.getValueFor(e),qe.getValueFor(e),Ye.getValueFor(e),Je.getValueFor(e),Ke.getValueFor(e))}),Rt=he("accent-fill-rest").withDefault((e=>Nt.getValueFor(e).evaluate(e).rest)),At=he("accent-fill-hover").withDefault((e=>Nt.getValueFor(e).evaluate(e).hover)),It=he("accent-fill-active").withDefault((e=>Nt.getValueFor(e).evaluate(e).active)),Mt=he("accent-fill-focus").withDefault((e=>Nt.getValueFor(e).evaluate(e).focus)),Pt=e=>(t,o)=>function(e,t){return e.contrast(le)>=t?le:ne}(o||Rt.getValueFor(t),e),Gt=ue("foreground-on-accent-recipe").withDefault({evaluate:(e,t)=>Pt(Ot.normal)(e,t)}),_t=he("foreground-on-accent-rest").withDefault((e=>Gt.getValueFor(e).evaluate(e,Rt.getValueFor(e)))),Et=he("foreground-on-accent-hover").withDefault((e=>Gt.getValueFor(e).evaluate(e,At.getValueFor(e)))),qt=he("foreground-on-accent-active").withDefault((e=>Gt.getValueFor(e).evaluate(e,It.getValueFor(e)))),Wt=he("foreground-on-accent-focus").withDefault((e=>Gt.getValueFor(e).evaluate(e,Mt.getValueFor(e)))),Ut=ue("foreground-on-accent-large-recipe").withDefault({evaluate:(e,t)=>Pt(Ot.large)(e,t)}),Xt=he("foreground-on-accent-rest-large").withDefault((e=>Ut.getValueFor(e).evaluate(e,Rt.getValueFor(e)))),Zt=he("foreground-on-accent-hover-large").withDefault((e=>Ut.getValueFor(e).evaluate(e,At.getValueFor(e)))),Yt=he("foreground-on-accent-active-large").withDefault((e=>Ut.getValueFor(e).evaluate(e,It.getValueFor(e)))),Jt=he("foreground-on-accent-focus-large").withDefault((e=>Ut.getValueFor(e).evaluate(e,Mt.getValueFor(e)))),Kt=he({name:"accent-foreground-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>(e=>(t,o)=>function(e,t,o,r,a,i,l){const n=e.source,s=e.closestIndexOf(n),c=Q(t),d=s+(1===c?Math.min(r,a):Math.max(c*r,c*a)),h=e.colorContrast(t,o,d,c),u=e.closestIndexOf(h),p=u+c*Math.abs(r-a);let g,b;return(1===c?r<a:c*r>c*a)?(g=u,b=p):(g=p,b=u),{rest:e.get(g),hover:e.get(b),active:e.get(g+c*i),focus:e.get(g+c*l)}}(yt.getValueFor(t),o||Lt.getValueFor(t),e,We.getValueFor(t),Ue.getValueFor(t),Xe.getValueFor(t),Ze.getValueFor(t)))(Ot.normal)(e,t)}),Qt=he("accent-foreground-rest").withDefault((e=>Kt.getValueFor(e).evaluate(e).rest)),eo=he("accent-foreground-hover").withDefault((e=>Kt.getValueFor(e).evaluate(e).hover)),to=he("accent-foreground-active").withDefault((e=>Kt.getValueFor(e).evaluate(e).active)),oo=he("accent-foreground-focus").withDefault((e=>Kt.getValueFor(e).evaluate(e).focus)),ro=he({name:"neutral-fill-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>function(e,t,o,r,a,i){const l=e.closestIndexOf(t),n=l>=Math.max(o,r,a,i)?-1:1;return{rest:e.get(l+n*o),hover:e.get(l+n*r),active:e.get(l+n*a),focus:e.get(l+n*i)}}(mt.getValueFor(e),t||Lt.getValueFor(e),Ye.getValueFor(e),Je.getValueFor(e),Ke.getValueFor(e),Qe.getValueFor(e))}),ao=he("neutral-fill-rest").withDefault((e=>ro.getValueFor(e).evaluate(e).rest)),io=he("neutral-fill-hover").withDefault((e=>ro.getValueFor(e).evaluate(e).hover)),lo=he("neutral-fill-active").withDefault((e=>ro.getValueFor(e).evaluate(e).active)),no=he("neutral-fill-focus").withDefault((e=>ro.getValueFor(e).evaluate(e).focus)),so=he({name:"neutral-fill-input-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>function(e,t,o,r,a,i){const l=Q(t),n=e.closestIndexOf(t);return{rest:e.get(n-l*o),hover:e.get(n-l*r),active:e.get(n-l*a),focus:e.get(n-l*i)}}(mt.getValueFor(e),t||Lt.getValueFor(e),et.getValueFor(e),tt.getValueFor(e),ot.getValueFor(e),rt.getValueFor(e))}),co=he("neutral-fill-input-rest").withDefault((e=>so.getValueFor(e).evaluate(e).rest)),ho=he("neutral-fill-input-hover").withDefault((e=>so.getValueFor(e).evaluate(e).hover)),uo=he("neutral-fill-input-active").withDefault((e=>so.getValueFor(e).evaluate(e).active)),po=he("neutral-fill-input-focus").withDefault((e=>so.getValueFor(e).evaluate(e).focus)),go=he({name:"neutral-fill-stealth-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>function(e,t,o,r,a,i,l,n,s,c){const d=Math.max(o,r,a,i,l,n,s,c),h=e.closestIndexOf(t),u=h>=d?-1:1;return{rest:e.get(h+u*o),hover:e.get(h+u*r),active:e.get(h+u*a),focus:e.get(h+u*i)}}(mt.getValueFor(e),t||Lt.getValueFor(e),at.getValueFor(e),it.getValueFor(e),lt.getValueFor(e),nt.getValueFor(e),Ye.getValueFor(e),Je.getValueFor(e),Ke.getValueFor(e),Qe.getValueFor(e))}),bo=he("neutral-fill-stealth-rest").withDefault((e=>go.getValueFor(e).evaluate(e).rest)),fo=he("neutral-fill-stealth-hover").withDefault((e=>go.getValueFor(e).evaluate(e).hover)),$o=he("neutral-fill-stealth-active").withDefault((e=>go.getValueFor(e).evaluate(e).active)),xo=he("neutral-fill-stealth-focus").withDefault((e=>go.getValueFor(e).evaluate(e).focus)),mo=he({name:"neutral-fill-strong-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>function(e,t,o,r,a,i){const l=Q(t),n=e.closestIndexOf(e.colorContrast(t,4.5)),s=n+l*Math.abs(o-r);let c,d;return(1===l?o<r:l*o>l*r)?(c=n,d=s):(c=s,d=n),{rest:e.get(c),hover:e.get(d),active:e.get(c+l*a),focus:e.get(c+l*i)}}(mt.getValueFor(e),t||Lt.getValueFor(e),st.getValueFor(e),ct.getValueFor(e),dt.getValueFor(e),ht.getValueFor(e))}),vo=he("neutral-fill-strong-rest").withDefault((e=>mo.getValueFor(e).evaluate(e).rest)),yo=he("neutral-fill-strong-hover").withDefault((e=>mo.getValueFor(e).evaluate(e).hover)),wo=he("neutral-fill-strong-active").withDefault((e=>mo.getValueFor(e).evaluate(e).active)),ko=he("neutral-fill-strong-focus").withDefault((e=>mo.getValueFor(e).evaluate(e).focus)),Fo=ue("neutral-fill-layer-recipe").withDefault({evaluate:(e,t)=>function(e,t,o){const r=e.closestIndexOf(t);return e.get(r-(r<o?-1*o:o))}(mt.getValueFor(e),t||Lt.getValueFor(e),ut.getValueFor(e))}),To=he("neutral-fill-layer-rest").withDefault((e=>Fo.getValueFor(e).evaluate(e))),Co=ue("focus-stroke-outer-recipe").withDefault({evaluate:e=>{return t=mt.getValueFor(e),o=Lt.getValueFor(e),t.colorContrast(o,3.5);var t,o}}),Vo=he("focus-stroke-outer").withDefault((e=>Co.getValueFor(e).evaluate(e))),Do=ue("focus-stroke-inner-recipe").withDefault({evaluate:e=>{return t=yt.getValueFor(e),o=Lt.getValueFor(e),r=Vo.getValueFor(e),t.colorContrast(r,3.5,t.closestIndexOf(t.source),-1*Q(o));var t,o,r}}),So=he("focus-stroke-inner").withDefault((e=>Do.getValueFor(e).evaluate(e))),Bo=ue("neutral-foreground-hint-recipe").withDefault({evaluate:e=>{return t=mt.getValueFor(e),o=Lt.getValueFor(e),t.colorContrast(o,4.5);var t,o}}),zo=he("neutral-foreground-hint").withDefault((e=>Bo.getValueFor(e).evaluate(e))),jo=ue("neutral-foreground-recipe").withDefault({evaluate:e=>{return t=mt.getValueFor(e),o=Lt.getValueFor(e),t.colorContrast(o,14);var t,o}}),Ho=he("neutral-foreground-rest").withDefault((e=>jo.getValueFor(e).evaluate(e))),Lo=he({name:"neutral-stroke-recipe",cssCustomPropertyName:null}).withDefault({evaluate:e=>function(e,t,o,r,a,i){const l=e.closestIndexOf(t),n=Q(t),s=l+n*o,c=s+n*(r-o),d=s+n*(a-o),h=s+n*(i-o);return{rest:e.get(s),hover:e.get(c),active:e.get(d),focus:e.get(h)}}(mt.getValueFor(e),Lt.getValueFor(e),pt.getValueFor(e),gt.getValueFor(e),bt.getValueFor(e),ft.getValueFor(e))}),Oo=he("neutral-stroke-rest").withDefault((e=>Lo.getValueFor(e).evaluate(e).rest)),No=he("neutral-stroke-hover").withDefault((e=>Lo.getValueFor(e).evaluate(e).hover)),Ro=he("neutral-stroke-active").withDefault((e=>Lo.getValueFor(e).evaluate(e).active)),Ao=he("neutral-stroke-focus").withDefault((e=>Lo.getValueFor(e).evaluate(e).focus)),Io=ue("neutral-stroke-divider-recipe").withDefault({evaluate:(e,t)=>function(e,t,o){return e.get(e.closestIndexOf(t)+Q(t)*o)}(mt.getValueFor(e),t||Lt.getValueFor(e),$t.getValueFor(e))}),Mo=he("neutral-stroke-divider-rest").withDefault((e=>Io.getValueFor(e).evaluate(e))),Po=(ae.DesignToken.create({name:"height-number",cssCustomPropertyName:null}).withDefault((e=>(ge.getValueFor(e)+xe.getValueFor(e))*me.getValueFor(e))),"data-jp-theme-name"),Go="data-jp-theme-light",_o="--jp-layout-color1";let Eo=!1;function qo(){Eo||(Eo=!0,function(){const e=()=>{new MutationObserver((()=>{Xo()})).observe(document.body,{attributes:!0,attributeFilter:[Po],childList:!1,characterData:!1}),Xo()};"complete"===document.readyState?e():window.addEventListener("load",e)}())}const Wo=e=>{const t=parseInt(e,10);return isNaN(t)?null:t},Uo={"--jp-border-width":{converter:Wo,token:we},"--jp-border-radius":{converter:Wo,token:$e},[_o]:{converter:(e,t)=>{const o=$(e);if(o){const e=V(o),t=D(x.fromObject({h:e.h,s:e.s,l:.5}));return ee.from(Y.create(t.r,t.g,t.b))}return null},token:mt},"--jp-brand-color1":{converter:(e,t)=>{const o=$(e);if(o){const e=V(o),r=t?1:-1,a=D(x.fromObject({h:e.h,s:e.s,l:e.l+r*_e.getValueFor(document.body)/94}));return ee.from(Y.create(a.r,a.g,a.b))}return null},token:yt},"--jp-ui-font-family":{token:pe},"--jp-ui-font-size1":{token:Fe}};function Xo(){var e;const t=getComputedStyle(document.body),o=document.body.getAttribute(Go);let r=!1;if(o)r="false"===o;else{const e=t.getPropertyValue(_o).toString();if(e){const t=$(e);t&&(r=R(Y.create(t.r,t.g,t.b)),console.debug(`Theme is ${r?"dark":"light"} based on '${_o}' value: ${e}.`))}}fe.setValueFor(document.body,r?re.DarkMode:re.LightMode);for(const o in Uo){const a=Uo[o],i=t.getPropertyValue(o).toString();if(document.body&&""!==i){const t=(null!==(e=a.converter)&&void 0!==e?e:e=>e)(i.trim(),r);null!==t?a.token.setValueFor(document.body,t):console.error(`Fail to parse value '${i}' for '${o}' as FAST design token.`)}}}const Zo=Y.create(1,1,1),Yo=Y.create(0,0,0),Jo=f("#D32F2F");var Ko;function Qo(e,t,o,r,a,i,l,n,s){const c=e.source,d=t.closestIndexOf(o)>=Math.max(l,n,s)?-1:1,h=e.closestIndexOf(c),u=h+-1*d*r,p=u+d*a,g=u+d*i;return{rest:e.get(u),hover:e.get(h),active:e.get(p),focus:e.get(g)}}function er(e,t,o,r,a,i,l){const n=e.source,s=e.closestIndexOf(n),c=R(t)?-1:1,d=s+(1===c?Math.min(r,a):Math.max(c*r,c*a)),h=e.colorContrast(t,o,d,c),u=e.closestIndexOf(h),p=u+c*Math.abs(r-a);let g,b;return(1===c?r<a:c*r>c*a)?(g=u,b=p):(g=p,b=u),{rest:e.get(g),hover:e.get(b),active:e.get(g+c*i),focus:e.get(g+c*l)}}function tr(e,t){return e.contrast(Zo)>=t?Zo:Yo}!function(e){e[e.normal=4.5]="normal",e[e.large=7]="large"}(Ko||(Ko={}));const or=Y.create(Jo.r,Jo.g,Jo.b);var rr=o(544);class ar{constructor(e,t){this.cache=new WeakMap,this.ltr=e,this.rtl=t}bind(e){this.attach(e)}unbind(e){const t=this.cache.get(e);t&&ve.unsubscribe(t)}attach(e){const t=this.cache.get(e)||new ir(this.ltr,this.rtl,e),o=ve.getValueFor(e);ve.subscribe(t),t.attach(o),this.cache.set(e,t)}}class ir{constructor(e,t,o){this.ltr=e,this.rtl=t,this.source=o,this.attached=null}handleChange({target:e,token:t}){this.attach(t.getValueFor(e))}attach(e){this.attached!==this[e]&&(null!==this.attached&&this.source.$fastController.removeStyles(this.attached),this.attached=this[e],null!==this.attached&&this.source.$fastController.addStyles(this.attached))}}const{create:lr}=rr.DesignToken,nr=lr({name:"error-palette",cssCustomPropertyName:null}).withDefault(ee.from(or)),sr=lr({name:"error-fill-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>Qo(nr.getValueFor(e),mt.getValueFor(e),t||Lt.getValueFor(e),_e.getValueFor(e),Ee.getValueFor(e),qe.getValueFor(e),Ye.getValueFor(e),Je.getValueFor(e),Ke.getValueFor(e))}),cr=lr("error-fill-rest").withDefault((e=>sr.getValueFor(e).evaluate(e).rest)),dr=lr("error-fill-hover").withDefault((e=>sr.getValueFor(e).evaluate(e).hover)),hr=lr("error-fill-active").withDefault((e=>sr.getValueFor(e).evaluate(e).active)),ur=lr("error-fill-focus").withDefault((e=>sr.getValueFor(e).evaluate(e).focus)),pr=e=>(t,o)=>tr(o||cr.getValueFor(t),e),gr=lr({name:"foreground-on-error-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>pr(Ko.normal)(e,t)}),br=lr("foreground-on-error-rest").withDefault((e=>gr.getValueFor(e).evaluate(e,cr.getValueFor(e)))),fr=lr("foreground-on-error-hover").withDefault((e=>gr.getValueFor(e).evaluate(e,dr.getValueFor(e)))),$r=lr("foreground-on-error-active").withDefault((e=>gr.getValueFor(e).evaluate(e,hr.getValueFor(e)))),xr=lr("foreground-on-error-focus").withDefault((e=>gr.getValueFor(e).evaluate(e,ur.getValueFor(e)))),mr=lr({name:"foreground-on-error-large-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>pr(Ko.large)(e,t)}),vr=lr("foreground-on-error-rest-large").withDefault((e=>mr.getValueFor(e).evaluate(e,cr.getValueFor(e)))),yr=lr("foreground-on-error-hover-large").withDefault((e=>mr.getValueFor(e).evaluate(e,dr.getValueFor(e)))),wr=lr("foreground-on-error-active-large").withDefault((e=>mr.getValueFor(e).evaluate(e,hr.getValueFor(e)))),kr=lr("foreground-on-error-focus-large").withDefault((e=>mr.getValueFor(e).evaluate(e,ur.getValueFor(e)))),Fr=lr({name:"error-foreground-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>(e=>(t,o)=>er(nr.getValueFor(t),o||Lt.getValueFor(t),e,We.getValueFor(t),Ue.getValueFor(t),Xe.getValueFor(t),Ze.getValueFor(t)))(Ko.normal)(e,t)}),Tr=lr("error-foreground-rest").withDefault((e=>Fr.getValueFor(e).evaluate(e).rest)),Cr=lr("error-foreground-hover").withDefault((e=>Fr.getValueFor(e).evaluate(e).hover)),Vr=lr("error-foreground-active").withDefault((e=>Fr.getValueFor(e).evaluate(e).active)),Dr=lr("error-foreground-focus").withDefault((e=>Fr.getValueFor(e).evaluate(e).focus));function Sr(e){return rr.DesignSystem.getOrCreate(e).withPrefix("jp")}var Br=o(68);const zr=(e,t)=>Br.css`
        ${(0,ae.display)("flex")} :host {
            box-sizing: border-box;
            flex-direction: column;
            font-family: ${pe};
            font-size: ${Ce};
            line-height: ${Ve};
            color: ${Ho};
            border-top: calc(${we} * 1px) solid ${Mo};
        }
    `;var jr,Hr=o(351);!function(e){e.Canvas="Canvas",e.CanvasText="CanvasText",e.LinkText="LinkText",e.VisitedText="VisitedText",e.ActiveText="ActiveText",e.ButtonFace="ButtonFace",e.ButtonText="ButtonText",e.Field="Field",e.FieldText="FieldText",e.Highlight="Highlight",e.HighlightText="HighlightText",e.GrayText="GrayText"}(jr||(jr={}));const Lr=Hr.cssPartial`(${ge} + ${xe}) * ${me}`,Or=(e,t)=>Hr.css`
    ${(0,rr.display)("flex")} :host {
      box-sizing: border-box;
      font-family: ${pe};
      flex-direction: column;
      font-size: ${Ce};
      line-height: ${Ve};
      border-bottom: calc(${we} * 1px) solid
        ${Mo};
    }

    .region {
      display: none;
      padding: calc((6 + (${me} * 2 * ${xe})) * 1px);
    }

    div.heading {
      display: grid;
      position: relative;
      grid-template-columns: calc(${Lr} * 1px) auto 1fr auto;
      color: ${Ho};
    }

    .button {
      appearance: none;
      border: none;
      background: none;
      grid-column: 3;
      outline: none;
      padding: 0 calc((6 + (${me} * 2 * ${xe})) * 1px);
      text-align: left;
      height: calc(${Lr} * 1px);
      color: currentcolor;
      cursor: pointer;
      font-family: inherit;
    }

    .button:hover {
      color: currentcolor;
    }

    .button:active {
      color: currentcolor;
    }

    .button::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      cursor: pointer;
    }

    /* prettier-ignore */
    .button:${rr.focusVisible}::before {
      outline: none;
      border: calc(${ke} * 1px) solid ${Mt};
      border-radius: calc(${$e} * 1px);
    }

    :host([expanded]) .region {
      display: block;
    }

    .icon {
      display: flex;
      align-items: center;
      justify-content: center;
      grid-column: 1;
      grid-row: 1;
      pointer-events: none;
      position: relative;
    }

    slot[name='expanded-icon'],
    slot[name='collapsed-icon'] {
      fill: currentcolor;
    }

    slot[name='collapsed-icon'] {
      display: flex;
    }

    :host([expanded]) slot[name='collapsed-icon'] {
      display: none;
    }

    slot[name='expanded-icon'] {
      display: none;
    }

    :host([expanded]) slot[name='expanded-icon'] {
      display: flex;
    }

    .start {
      display: flex;
      align-items: center;
      padding-inline-start: calc(${me} * 1px);
      justify-content: center;
      grid-column: 2;
      position: relative;
    }

    .end {
      display: flex;
      align-items: center;
      justify-content: center;
      grid-column: 4;
      position: relative;
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      /* prettier-ignore */
      .button:${rr.focusVisible}::before {
          border-color: ${jr.Highlight};
        }
      :host slot[name='collapsed-icon'],
      :host([expanded]) slot[name='expanded-icon'] {
        fill: ${jr.ButtonText};
      }
    `)),Nr=rr.AccordionItem.compose({baseName:"accordion-item",template:rr.accordionItemTemplate,styles:Or,collapsedIcon:'\n      <svg\n        width="20"\n        height="20"\n        viewBox="0 0 16 16"\n        xmlns="http://www.w3.org/2000/svg"\n        class="expand-collapse-glyph"\n      >\n        <path\n          fill-rule="evenodd"\n          clip-rule="evenodd"\n          d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"\n        />\n      </svg>\n    ',expandedIcon:'\n      <svg\n        width="20"\n        height="20"\n        viewBox="0 0 16 16"\n        xmlns="http://www.w3.org/2000/svg"\n        class="expand-collapse-glyph"\n      >\n        <path\n          fill-rule="evenodd"\n          clip-rule="evenodd"\n          transform="rotate(90,8,8)"\n          d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"\n        />\n      </svg>\n    '}),Rr=rr.Accordion.compose({baseName:"accordion",template:rr.accordionTemplate,styles:zr});var Ar,Ir=o(655);!function(e){e.Canvas="Canvas",e.CanvasText="CanvasText",e.LinkText="LinkText",e.VisitedText="VisitedText",e.ActiveText="ActiveText",e.ButtonFace="ButtonFace",e.ButtonText="ButtonText",e.Field="Field",e.FieldText="FieldText",e.Highlight="Highlight",e.HighlightText="HighlightText",e.GrayText="GrayText"}(Ar||(Ar={}));const Mr=Br.cssPartial`(${ge} + ${xe}) * ${me}`,Pr=Br.css`
    ${(0,ae.display)("inline-flex")} :host {
        font-family: ${pe};
        outline: none;
        font-size: ${Fe};
        line-height: ${Te};
        height: calc(${Mr} * 1px);
        min-width: calc(${Mr} * 1px);
        background-color: ${ao};
        color: ${Ho};
        border-radius: calc(${$e} * 1px);
        fill: currentcolor;
        cursor: pointer;
    }

    .control {
        background: transparent;
        height: inherit;
        flex-grow: 1;
        box-sizing: border-box;
        display: inline-flex;
        justify-content: center;
        align-items: baseline;
        padding: 0 calc((10 + (${me} * 2 * ${xe})) * 1px);
        white-space: nowrap;
        outline: none;
        text-decoration: none;
        border: calc(${we} * 1px) solid transparent;
        color: inherit;
        border-radius: inherit;
        fill: inherit;
        cursor: inherit;
        font-weight: inherit;
        font-family: inherit;
        font-size: inherit;
        line-height: inherit;
    }

    :host(:hover) {
        background-color: ${io};
    }

    :host(:active) {
        background-color: ${lo};
    }

    .control:${ae.focusVisible} {
        border-color: ${Vo};
        box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px) ${Vo} inset;
    }

    .control::-moz-focus-inner {
        border: 0;
    }

    .start,
    .content,
    .end {
        align-self: center;
    }

    .start,
    .end {
        display: flex;
    }

    .control.icon-only {
        padding: 0;
        line-height: 0;
    }

    ::slotted(svg) {
        ${""} width: 16px;
        height: 16px;
        pointer-events: none;
    }

    .start {
        margin-inline-end: 11px;
    }

    .end {
        margin-inline-start: 11px;
    }
`.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
            :host .control {
              background-color: ${Ar.ButtonFace};
              border-color: ${Ar.ButtonText};
              color: ${Ar.ButtonText};
              fill: currentColor;
            }

            :host(:hover) .control {
              forced-color-adjust: none;
              background-color: ${Ar.Highlight};
              color: ${Ar.HighlightText};
            }

            .control:${ae.focusVisible} {
              forced-color-adjust: none;
              background-color: ${Ar.Highlight};
              border-color: ${Ar.ButtonText};
              box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px) ${Ar.ButtonText} inset;
              color: ${Ar.HighlightText};
            }

            .control:hover,
            :host([appearance="outline"]) .control:hover {
              border-color: ${Ar.ButtonText};
            }

            :host([href]) .control {
                border-color: ${Ar.LinkText};
                color: ${Ar.LinkText};
            }

            :host([href]) .control:hover,
            :host([href]) .control:${ae.focusVisible}{
              forced-color-adjust: none;
              background: ${Ar.ButtonFace};
              border-color: ${Ar.LinkText};
              box-shadow: 0 0 0 1px ${Ar.LinkText} inset;
              color: ${Ar.LinkText};
              fill: currentColor;
            }
        `)),Gr=Br.css`
    :host([appearance="accent"]) {
        background: ${Rt};
        color: ${_t};
    }

    :host([appearance="accent"]:hover) {
        background: ${At};
        color: ${Et};
    }

    :host([appearance="accent"]:active) .control:active {
        background: ${It};
        color: ${qt};
    }

    :host([appearance="accent"]) .control:${ae.focusVisible} {
        box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px) ${Vo} inset,
            0 0 0 calc((${ke} + ${we}) * 1px) ${So} inset;
    }
`.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
            :host([appearance="accent"]) .control {
                forced-color-adjust: none;
                background: ${Ar.Highlight};
                color: ${Ar.HighlightText};
            }

            :host([appearance="accent"]) .control:hover,
            :host([appearance="accent"]:active) .control:active {
                background: ${Ar.HighlightText};
                border-color: ${Ar.Highlight};
                color: ${Ar.Highlight};
            }

            :host([appearance="accent"]) .control:${ae.focusVisible} {
                border-color: ${Ar.Highlight};
                box-shadow: 0 0 0 calc(${ke} * 1px) ${Ar.HighlightText} inset;
            }

            :host([appearance="accent"][href]) .control{
                background: ${Ar.LinkText};
                color: ${Ar.HighlightText};
            }

            :host([appearance="accent"][href]) .control:hover {
                background: ${Ar.ButtonFace};
                border-color: ${Ar.LinkText};
                box-shadow: none;
                color: ${Ar.LinkText};
                fill: currentColor;
            }

            :host([appearance="accent"][href]) .control:${ae.focusVisible} {
                border-color: ${Ar.LinkText};
                box-shadow: 0 0 0 calc(${ke} * 1px) ${Ar.HighlightText} inset;
            }
        `)),_r=Br.css`
    :host([appearance="hypertext"]) {
        font-size: inherit;
        line-height: inherit;
        height: auto;
        min-width: 0;
        background: transparent;
    }

    :host([appearance="hypertext"]) .control {
        display: inline;
        padding: 0;
        border: none;
        box-shadow: none;
        border-radius: 0;
        line-height: 1;
    }

    :host a.control:not(:link) {
        background-color: transparent;
        cursor: default;
    }
    :host([appearance="hypertext"]) .control:link,
    :host([appearance="hypertext"]) .control:visited {
        background: transparent;
        color: ${Qt};
        border-bottom: calc(${we} * 1px) solid ${Qt};
    }

    :host([appearance="hypertext"]:hover),
    :host([appearance="hypertext"]) .control:hover {
        background: transparent;
        border-bottom-color: ${eo};
    }

    :host([appearance="hypertext"]:active),
    :host([appearance="hypertext"]) .control:active {
        background: transparent;
        border-bottom-color: ${to};
    }

    :host([appearance="hypertext"]) .control:${ae.focusVisible} {
        border-bottom: calc(${ke} * 1px) solid ${Vo};
        margin-bottom: calc(calc(${we} - ${ke}) * 1px);
    }
`.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
            :host([appearance="hypertext"]:hover) {
                background-color: ${Ar.ButtonFace};
                color: ${Ar.ButtonText};
            }
            :host([appearance="hypertext"][href]) .control:hover,
            :host([appearance="hypertext"][href]) .control:active,
            :host([appearance="hypertext"][href]) .control:${ae.focusVisible} {
                color: ${Ar.LinkText};
                border-bottom-color: ${Ar.LinkText};
                box-shadow: none;
            }
        `)),Er=Br.css`
    :host([appearance="lightweight"]) {
        background: transparent;
        color: ${Qt};
    }

    :host([appearance="lightweight"]) .control {
        padding: 0;
        height: initial;
        border: none;
        box-shadow: none;
        border-radius: 0;
    }

    :host([appearance="lightweight"]:hover) {
        background: transparent;
        color: ${eo};
    }

    :host([appearance="lightweight"]:active) {
        background: transparent;
        color: ${to};
    }

    :host([appearance="lightweight"]) .content {
        position: relative;
    }

    :host([appearance="lightweight"]) .content::before {
        content: "";
        display: block;
        height: calc(${we} * 1px);
        position: absolute;
        top: calc(1em + 4px);
        width: 100%;
    }

    :host([appearance="lightweight"]:hover) .content::before {
        background: ${eo};
    }

    :host([appearance="lightweight"]:active) .content::before {
        background: ${to};
    }

    :host([appearance="lightweight"]) .control:${ae.focusVisible} .content::before {
        background: ${Ho};
        height: calc(${ke} * 1px);
    }
`.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
            :host([appearance="lightweight"]) .control:hover,
            :host([appearance="lightweight"]) .control:${ae.focusVisible} {
                forced-color-adjust: none;
                background: ${Ar.ButtonFace};
                color: ${Ar.Highlight};
            }
            :host([appearance="lightweight"]) .control:hover .content::before,
            :host([appearance="lightweight"]) .control:${ae.focusVisible} .content::before {
                background: ${Ar.Highlight};
            }

            :host([appearance="lightweight"][href]) .control:hover,
            :host([appearance="lightweight"][href]) .control:${ae.focusVisible} {
                background: ${Ar.ButtonFace};
                box-shadow: none;
                color: ${Ar.LinkText};
            }

            :host([appearance="lightweight"][href]) .control:hover .content::before,
            :host([appearance="lightweight"][href]) .control:${ae.focusVisible} .content::before {
                background: ${Ar.LinkText};
            }
        `)),qr=Br.css`
    :host([appearance="outline"]) {
        background: transparent;
        border-color: ${Rt};
    }

    :host([appearance="outline"]:hover) {
        border-color: ${At};
    }

    :host([appearance="outline"]:active) {
        border-color: ${It};
    }

    :host([appearance="outline"]) .control {
        border-color: inherit;
    }

    :host([appearance="outline"]) .control:${ae.focusVisible} {
        box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px) ${Vo} inset;
        border-color: ${Vo};
    }
`.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
            :host([appearance="outline"]) .control {
                border-color: ${Ar.ButtonText};
            }
            :host([appearance="outline"]) .control:${ae.focusVisible} {
              forced-color-adjust: none;
              background-color: ${Ar.Highlight};
              border-color: ${Ar.ButtonText};
              box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px) ${Ar.ButtonText} inset;
              color: ${Ar.HighlightText};
              fill: currentColor;
            }
            :host([appearance="outline"][href]) .control {
                background: ${Ar.ButtonFace};
                border-color: ${Ar.LinkText};
                color: ${Ar.LinkText};
                fill: currentColor;
            }
            :host([appearance="outline"][href]) .control:hover,
            :host([appearance="outline"][href]) .control:${ae.focusVisible} {
              forced-color-adjust: none;
              border-color: ${Ar.LinkText};
              box-shadow: 0 0 0 1px ${Ar.LinkText} inset;
            }
        `)),Wr=Br.css`
    :host([appearance="stealth"]) {
        background: ${bo};
    }

    :host([appearance="stealth"]:hover) {
        background: ${fo};
    }

    :host([appearance="stealth"]:active) {
        background: ${$o};
    }
`.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
            :host([appearance="stealth"]),
            :host([appearance="stealth"]) .control {
                forced-color-adjust: none;
                background: ${Ar.ButtonFace};
                border-color: transparent;
                color: ${Ar.ButtonText};
                fill: currentColor;
            }

            :host([appearance="stealth"]:hover) .control {
                background: ${Ar.Highlight};
                border-color: ${Ar.Highlight};
                color: ${Ar.HighlightText};
                fill: currentColor;
            }

            :host([appearance="stealth"]:${ae.focusVisible}) .control {
                background: ${Ar.Highlight};
                box-shadow: 0 0 0 1px ${Ar.Highlight};
                color: ${Ar.HighlightText};
                fill: currentColor;
            }

            :host([appearance="stealth"][href]) .control {
                color: ${Ar.LinkText};
            }

            :host([appearance="stealth"][href]:hover) .control,
            :host([appearance="stealth"][href]:${ae.focusVisible}) .control {
                background: ${Ar.LinkText};
                border-color: ${Ar.LinkText};
                color: ${Ar.HighlightText};
                fill: currentColor;
            }

            :host([appearance="stealth"][href]:${ae.focusVisible}) .control {
                forced-color-adjust: none;
                box-shadow: 0 0 0 1px ${Ar.LinkText};
            }
        `));function Ur(e,t){return new ae.PropertyStyleSheetBehavior("appearance",e,t)}const Xr=(e,t)=>Br.css`
        ${Pr}
    `.withBehaviors(Ur("accent",Gr),Ur("hypertext",_r),Ur("lightweight",Er),Ur("outline",qr),Ur("stealth",Wr));class Zr extends ae.Anchor{appearanceChanged(e,t){this.$fastController.isConnected&&(this.classList.remove(e),this.classList.add(t))}connectedCallback(){super.connectedCallback(),this.appearance||(this.appearance="neutral")}defaultSlottedContentChanged(e,t){const o=this.defaultSlottedContent.filter((e=>e.nodeType===Node.ELEMENT_NODE));1===o.length&&o[0]instanceof SVGElement?this.control.classList.add("icon-only"):this.control.classList.remove("icon-only")}}(0,Ir.gn)([Br.attr],Zr.prototype,"appearance",void 0),Zr.compose({baseName:"anchor",baseClass:ae.Anchor,template:ae.anchorTemplate,styles:Xr,shadowOptions:{delegatesFocus:!0}});const Yr=Zr.compose({baseName:"anchor",baseClass:rr.Anchor,template:rr.anchorTemplate,styles:Xr}),Jr=(e,t)=>Br.css`
    :host {
        contain: layout;
        display: block;
    }
`,Kr=rr.AnchoredRegion.compose({baseName:"anchored-region",template:rr.anchoredRegionTemplate,styles:Jr});class Qr extends ae.Avatar{}(0,Ir.gn)([(0,Br.attr)({attribute:"src"})],Qr.prototype,"imgSrc",void 0),(0,Ir.gn)([Br.attr],Qr.prototype,"alt",void 0);const ea=Br.html`
    ${(0,Br.when)((e=>e.imgSrc),Br.html`
            <img
                src="${e=>e.imgSrc}"
                alt="${e=>e.alt}"
                slot="media"
                class="media"
                part="media"
            />
        `)}
`,ta=(Qr.compose({baseName:"avatar",baseClass:ae.Avatar,template:ae.avatarTemplate,styles:(e,t)=>Br.css`
        ${(0,ae.display)("flex")} :host {
            position: relative;
            height: var(--avatar-size, var(--avatar-size-default));
            max-width: var(--avatar-size, var(--avatar-size-default));
            --avatar-size-default: calc(
                (
                        (${ge} + ${xe}) * ${me} +
                            ((${me} * 8) - 40)
                    ) * 1px
            );
            --avatar-text-size: ${Fe};
            --avatar-text-ratio: ${me};
        }

        .link {
            text-decoration: none;
            color: ${Ho};
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            min-width: 100%;
        }

        .square {
            border-radius: calc(${$e} * 1px);
            min-width: 100%;
            overflow: hidden;
        }

        .circle {
            border-radius: 100%;
            min-width: 100%;
            overflow: hidden;
        }

        .backplate {
            position: relative;
            display: flex;
        }

        .media,
        ::slotted(img) {
            max-width: 100%;
            position: absolute;
            display: block;
        }

        .content {
            font-size: calc(
                (var(--avatar-text-size) + var(--avatar-size, var(--avatar-size-default))) /
                    var(--avatar-text-ratio)
            );
            line-height: var(--avatar-size, var(--avatar-size-default));
            display: block;
            min-height: var(--avatar-size, var(--avatar-size-default));
        }

        ::slotted(${e.tagFor(ae.Badge)}) {
            position: absolute;
            display: block;
        }
    `.withBehaviors(new ar(((e,t)=>Br.css`
    ::slotted(${e.tagFor(ae.Badge)}) {
        right: 0;
    }
`)(e),((e,t)=>Br.css`
    ::slotted(${e.tagFor(ae.Badge)}) {
        left: 0;
    }
`)(e))),media:ea,shadowOptions:{delegatesFocus:!0}}),(e,t)=>Hr.css`
    ${(0,rr.display)("flex")} :host {
      position: relative;
      height: var(--avatar-size, var(--avatar-size-default));
      width: var(--avatar-size, var(--avatar-size-default));
      --avatar-size-default: calc(
        (
            (${ge} + ${xe}) * ${me} +
              ((${me} * 8) - 40)
          ) * 1px
      );
      --avatar-text-size: ${Fe};
      --avatar-text-ratio: ${me};
    }

    .link {
      text-decoration: none;
      color: ${Ho};
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      min-width: 100%;
    }

    .square {
      border-radius: calc(${$e} * 1px);
      min-width: 100%;
      overflow: hidden;
    }

    .circle {
      border-radius: 100%;
      min-width: 100%;
      overflow: hidden;
    }

    .backplate {
      position: relative;
      display: flex;
      background-color: ${Rt};
    }

    .media,
    ::slotted(img) {
      max-width: 100%;
      position: absolute;
      display: block;
    }

    .content {
      font-size: calc(
        (
            var(--avatar-text-size) +
              var(--avatar-size, var(--avatar-size-default))
          ) / var(--avatar-text-ratio)
      );
      color: ${_t};
      line-height: var(--avatar-size, var(--avatar-size-default));
      display: block;
      min-height: var(--avatar-size, var(--avatar-size-default));
    }

    ::slotted(${e.tagFor(rr.Badge)}) {
      position: absolute;
      display: block;
    }
  `.withBehaviors(new ar(((e,t)=>Hr.css`
  ::slotted(${e.tagFor(rr.Badge)}) {
    right: 0;
  }
`)(e),((e,t)=>Hr.css`
  ::slotted(${e.tagFor(rr.Badge)}) {
    left: 0;
  }
`)(e)))),oa=Qr.compose({baseName:"avatar",baseClass:rr.Avatar,template:rr.avatarTemplate,styles:ta,media:ea,shadowOptions:{delegatesFocus:!0}}),ra=(e,t)=>Hr.css`
  ${(0,rr.display)("inline-block")} :host {
    box-sizing: border-box;
    font-family: ${pe};
    font-size: ${Ce};
    line-height: ${Ve};
  }

  .control {
    border-radius: calc(${$e} * 1px);
    padding: calc(((${me} * 0.5) - ${we}) * 1px)
      calc((${me} - ${we}) * 1px);
    color: ${Ho};
    font-weight: 600;
    border: calc(${we} * 1px) solid transparent;
    background-color: ${ao};
  }

  .control[style] {
    font-weight: 400;
  }

  :host([circular]) .control {
    border-radius: 100px;
    padding: 0 calc(${me} * 1px);
    /* Need to work with Brian on width and height here */
    height: calc((${Lr} - (${me} * 3)) * 1px);
    min-width: calc((${Lr} - (${me} * 3)) * 1px);
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
  }
`,aa=rr.Badge.compose({baseName:"badge",template:rr.badgeTemplate,styles:ra}),ia=(e,t)=>Br.css`
    ${(0,ae.display)("inline-block")} :host {
        box-sizing: border-box;
        font-family: ${pe};
        font-size: ${Fe};
        line-height: ${Te};
    }

    .list {
        display: flex;
        flex-wrap: wrap;
    }
`,la=rr.Breadcrumb.compose({baseName:"breadcrumb",template:rr.breadcrumbTemplate,styles:ia}),na=(e,t)=>Hr.css`
    ${(0,rr.display)("inline-flex")} :host {
        background: transparent;
        box-sizing: border-box;
        font-family: ${pe};
        font-size: ${Fe};
        fill: currentColor;
        line-height: ${Te};
        min-width: calc(${Lr} * 1px);
        outline: none;
        color: ${Ho}
    }

    .listitem {
        display: flex;
        align-items: center;
        width: max-content;
    }

    .separator {
        margin: 0 6px;
        display: flex;
    }

    .control {
        align-items: center;
        box-sizing: border-box;
        color: ${Qt};
        cursor: pointer;
        display: flex;
        fill: inherit;
        outline: none;
        text-decoration: none;
        white-space: nowrap;
    }

    .control:hover {
        color: ${eo};
    }

    .control:active {
        color: ${to};
    }

    .control .content {
        position: relative;
    }

    .control .content::before {
        content: "";
        display: block;
        height: calc(${we} * 1px);
        left: 0;
        position: absolute;
        right: 0;
        top: calc(1em + 4px);
        width: 100%;
    }

    .control:hover .content::before {
        background: ${eo};
    }

    .control:active .content::before {
        background: ${to};
    }

    .control:${rr.focusVisible} .content::before {
        background: ${oo};
        height: calc(${ke} * 1px);
    }

    .control:not([href]) {
        color: ${Ho};
        cursor: default;
    }

    .control:not([href]) .content::before {
        background: none;
    }

    .start,
    .end {
        display: flex;
    }

    ::slotted(svg) {
        /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
        width: 16px;
        height: 16px;
    }

    .start {
        margin-inline-end: 6px;
    }

    .end {
        margin-inline-start: 6px;
    }
`.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      .control:hover .content::before,
                .control:${rr.focusVisible} .content::before {
        background: ${jr.LinkText};
      }
      .start,
      .end {
        fill: ${jr.ButtonText};
      }
    `)),sa=rr.BreadcrumbItem.compose({baseName:"breadcrumb-item",template:rr.breadcrumbItemTemplate,styles:na,separator:"/",shadowOptions:{delegatesFocus:!0}});function ca(e,t){return new rr.PropertyStyleSheetBehavior("appearance",e,t)}const da=Hr.css`
  ${(0,rr.display)("inline-flex")} :host {
    font-family: ${pe};
    outline: none;
    font-size: ${Fe};
    line-height: ${Te};
    height: calc(${Lr} * 1px);
    min-width: calc(${Lr} * 1px);
    background-color: ${ao};
    color: ${Ho};
    border-radius: calc(${$e} * 1px);
    fill: currentcolor;
    cursor: pointer;
    margin: calc((${ke} + 2) * 1px);
  }

  .control {
    background: transparent;
    height: inherit;
    flex-grow: 1;
    box-sizing: border-box;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    padding: 0 calc((10 + (${me} * 2 * ${xe})) * 1px);
    white-space: nowrap;
    outline: none;
    text-decoration: none;
    border: calc(${we} * 1px) solid transparent;
    color: inherit;
    border-radius: inherit;
    fill: inherit;
    cursor: inherit;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
  }

  :host(:hover) {
    background-color: ${io};
  }

  :host(:active) {
    background-color: ${lo};
  }

  :host([aria-pressed='true']) {
    box-shadow: inset 0px 0px 2px 2px ${wo};
  }

  :host([minimal]) {
    --density: -4;
  }

  :host([minimal]) .control {
    padding: 1px;
  }

  /* prettier-ignore */
  .control:${rr.focusVisible} {
    outline: calc(${ke} * 1px) solid ${ko};
    outline-offset: 2px;
    -moz-outline-radius: 0px;
  }

  .control::-moz-focus-inner {
    border: 0;
  }

  .start,
  .end {
    display: flex;
  }

  .control.icon-only {
    padding: 0;
    line-height: 0;
  }

  ::slotted(svg) {
    ${""} width: 16px;
    height: 16px;
    pointer-events: none;
  }

  .start {
    margin-inline-end: 11px;
  }

  .end {
    margin-inline-start: 11px;
  }
`.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
    :host .control {
      background-color: ${jr.ButtonFace};
      border-color: ${jr.ButtonText};
      color: ${jr.ButtonText};
      fill: currentColor;
    }

    :host(:hover) .control {
      forced-color-adjust: none;
      background-color: ${jr.Highlight};
      color: ${jr.HighlightText};
    }

    /* prettier-ignore */
    .control:${rr.focusVisible} {
        forced-color-adjust: none;
        background-color: ${jr.Highlight};
        outline-color: ${jr.ButtonText};
        color: ${jr.HighlightText};
      }

    .control:hover,
    :host([appearance='outline']) .control:hover {
      border-color: ${jr.ButtonText};
    }

    :host([href]) .control {
      border-color: ${jr.LinkText};
      color: ${jr.LinkText};
    }

    :host([href]) .control:hover,
      :host([href]) .control:${rr.focusVisible} {
      forced-color-adjust: none;
      background: ${jr.ButtonFace};
      outline-color: ${jr.LinkText};
      color: ${jr.LinkText};
      fill: currentColor;
    }
  `)),ha=Hr.css`
  :host([appearance='accent']) {
    background: ${Rt};
    color: ${_t};
  }

  :host([appearance='accent']:hover) {
    background: ${At};
    color: ${Et};
  }

  :host([appearance='accent'][aria-pressed='true']) {
    box-shadow: inset 0px 0px 2px 2px ${to};
  }

  :host([appearance='accent']:active) .control:active {
    background: ${It};
    color: ${qt};
  }

  :host([appearance="accent"]) .control:${rr.focusVisible} {
    outline-color: ${Mt};
  }
`.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
    :host([appearance='accent']) .control {
      forced-color-adjust: none;
      background: ${jr.Highlight};
      color: ${jr.HighlightText};
    }

    :host([appearance='accent']) .control:hover,
    :host([appearance='accent']:active) .control:active {
      background: ${jr.HighlightText};
      border-color: ${jr.Highlight};
      color: ${jr.Highlight};
    }

    :host([appearance="accent"]) .control:${rr.focusVisible} {
      outline-color: ${jr.Highlight};
    }

    :host([appearance='accent'][href]) .control {
      background: ${jr.LinkText};
      color: ${jr.HighlightText};
    }

    :host([appearance='accent'][href]) .control:hover {
      background: ${jr.ButtonFace};
      border-color: ${jr.LinkText};
      box-shadow: none;
      color: ${jr.LinkText};
      fill: currentColor;
    }

    :host([appearance="accent"][href]) .control:${rr.focusVisible} {
      outline-color: ${jr.HighlightText};
    }
  `)),ua=Hr.css`
  :host([appearance='error']) {
    background: ${cr};
    color: ${_t};
  }

  :host([appearance='error']:hover) {
    background: ${dr};
    color: ${Et};
  }

  :host([appearance='error'][aria-pressed='true']) {
    box-shadow: inset 0px 0px 2px 2px ${Vr};
  }

  :host([appearance='error']:active) .control:active {
    background: ${hr};
    color: ${qt};
  }

  :host([appearance="error"]) .control:${rr.focusVisible} {
    outline-color: ${ur};
  }
`.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
    :host([appearance='error']) .control {
      forced-color-adjust: none;
      background: ${jr.Highlight};
      color: ${jr.HighlightText};
    }

    :host([appearance='error']) .control:hover,
    :host([appearance='error']:active) .control:active {
      background: ${jr.HighlightText};
      border-color: ${jr.Highlight};
      color: ${jr.Highlight};
    }

    :host([appearance="error"]) .control:${rr.focusVisible} {
      outline-color: ${jr.Highlight};
    }

    :host([appearance='error'][href]) .control {
      background: ${jr.LinkText};
      color: ${jr.HighlightText};
    }

    :host([appearance='error'][href]) .control:hover {
      background: ${jr.ButtonFace};
      border-color: ${jr.LinkText};
      box-shadow: none;
      color: ${jr.LinkText};
      fill: currentColor;
    }

    :host([appearance="error"][href]) .control:${rr.focusVisible} {
      outline-color: ${jr.HighlightText};
    }
  `)),pa=Hr.css`
  :host([appearance='lightweight']) {
    background: transparent;
    color: ${Qt};
  }

  :host([appearance='lightweight']) .control {
    padding: 0;
    height: initial;
    border: none;
    box-shadow: none;
    border-radius: 0;
  }

  :host([appearance='lightweight']:hover) {
    background: transparent;
    color: ${eo};
  }

  :host([appearance='lightweight']:active) {
    background: transparent;
    color: ${to};
  }

  :host([appearance='lightweight']) .content {
    position: relative;
  }

  :host([appearance='lightweight']) .content::before {
    content: '';
    display: block;
    height: calc(${we} * 1px);
    position: absolute;
    top: calc(1em + 4px);
    width: 100%;
  }

  :host([appearance='lightweight']:hover) .content::before {
    background: ${eo};
  }

  :host([appearance='lightweight']:active) .content::before {
    background: ${to};
  }

  :host([appearance="lightweight"]) .control:${rr.focusVisible} {
    outline-color: transparent;
  }

  :host([appearance="lightweight"]) .control:${rr.focusVisible} .content::before {
    background: ${Ho};
    height: calc(${ke} * 1px);
  }
`.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
    :host([appearance="lightweight"]) .control:hover,
      :host([appearance="lightweight"]) .control:${rr.focusVisible} {
      forced-color-adjust: none;
      background: ${jr.ButtonFace};
      color: ${jr.Highlight};
    }
    :host([appearance="lightweight"]) .control:hover .content::before,
      :host([appearance="lightweight"]) .control:${rr.focusVisible} .content::before {
      background: ${jr.Highlight};
    }

    :host([appearance="lightweight"][href]) .control:hover,
      :host([appearance="lightweight"][href]) .control:${rr.focusVisible} {
      background: ${jr.ButtonFace};
      box-shadow: none;
      color: ${jr.LinkText};
    }

    :host([appearance="lightweight"][href]) .control:hover .content::before,
      :host([appearance="lightweight"][href]) .control:${rr.focusVisible} .content::before {
      background: ${jr.LinkText};
    }
  `)),ga=Hr.css`
  :host([appearance='outline']) {
    background: transparent;
    border-color: ${Rt};
  }

  :host([appearance='outline']:hover) {
    border-color: ${At};
  }

  :host([appearance='outline']:active) {
    border-color: ${It};
  }

  :host([appearance='outline']) .control {
    border-color: inherit;
  }

  :host([appearance="outline"]) .control:${rr.focusVisible} {
    outline-color: ${Mt};
  }
`.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
    :host([appearance='outline']) .control {
      border-color: ${jr.ButtonText};
    }
    :host([appearance="outline"]) .control:${rr.focusVisible} {
      forced-color-adjust: none;
      background-color: ${jr.Highlight};
      outline-color: ${jr.ButtonText};
      color: ${jr.HighlightText};
      fill: currentColor;
    }
    :host([appearance='outline'][href]) .control {
      background: ${jr.ButtonFace};
      border-color: ${jr.LinkText};
      color: ${jr.LinkText};
      fill: currentColor;
    }
    :host([appearance="outline"][href]) .control:hover,
      :host([appearance="outline"][href]) .control:${rr.focusVisible} {
      forced-color-adjust: none;
      outline-color: ${jr.LinkText};
    }
  `)),ba=Hr.css`
  :host([appearance='stealth']) {
    background: transparent;
  }

  :host([appearance='stealth']:hover) {
    background: ${fo};
  }

  :host([appearance='stealth']:active) {
    background: ${$o};
  }

  :host([appearance='stealth']) .control:${rr.focusVisible} {
    outline-color: ${Mt};
  }
`.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
    :host([appearance='stealth']),
    :host([appearance='stealth']) .control {
      forced-color-adjust: none;
      background: ${jr.ButtonFace};
      border-color: transparent;
      color: ${jr.ButtonText};
      fill: currentColor;
    }

    :host([appearance='stealth']:hover) .control {
      background: ${jr.Highlight};
      border-color: ${jr.Highlight};
      color: ${jr.HighlightText};
      fill: currentColor;
    }

    :host([appearance="stealth"]:${rr.focusVisible}) .control {
      outline-color: ${jr.Highlight};
      color: ${jr.HighlightText};
      fill: currentColor;
    }

    :host([appearance='stealth'][href]) .control {
      color: ${jr.LinkText};
    }

    :host([appearance="stealth"][href]:hover) .control,
      :host([appearance="stealth"][href]:${rr.focusVisible}) .control {
      background: ${jr.LinkText};
      border-color: ${jr.LinkText};
      color: ${jr.HighlightText};
      fill: currentColor;
    }

    :host([appearance="stealth"][href]:${rr.focusVisible}) .control {
      forced-color-adjust: none;
      box-shadow: 0 0 0 1px ${jr.LinkText};
    }
  `));class fa extends rr.Button{connectedCallback(){super.connectedCallback(),this.appearance||(this.appearance="neutral")}defaultSlottedContentChanged(e,t){const o=this.defaultSlottedContent.filter((e=>e.nodeType===Node.ELEMENT_NODE));1===o.length&&(o[0]instanceof SVGElement||o[0].classList.contains("fa")||o[0].classList.contains("fas"))?this.control.classList.add("icon-only"):this.control.classList.remove("icon-only")}}(0,Ir.gn)([Hr.attr],fa.prototype,"appearance",void 0),(0,Ir.gn)([(0,Hr.attr)({attribute:"minimal",mode:"boolean"})],fa.prototype,"minimal",void 0);const $a=fa.compose({baseName:"button",baseClass:rr.Button,template:rr.buttonTemplate,styles:(e,t)=>Hr.css`
    :host([disabled]),
    :host([disabled]:hover),
    :host([disabled]:active) {
      opacity: ${ye};
      background-color: ${ao};
      cursor: ${rr.disabledCursor};
    }

    ${da}
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      :host([disabled]),
      :host([disabled]) .control,
      :host([disabled]:hover),
      :host([disabled]:active) {
        forced-color-adjust: none;
        background-color: ${jr.ButtonFace};
        outline-color: ${jr.GrayText};
        color: ${jr.GrayText};
        cursor: ${rr.disabledCursor};
        opacity: 1;
      }
    `),ca("accent",Hr.css`
        :host([appearance='accent'][disabled]),
        :host([appearance='accent'][disabled]:hover),
        :host([appearance='accent'][disabled]:active) {
          background: ${Rt};
        }

        ${ha}
      `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
          :host([appearance='accent'][disabled]) .control,
          :host([appearance='accent'][disabled]) .control:hover {
            background: ${jr.ButtonFace};
            border-color: ${jr.GrayText};
            color: ${jr.GrayText};
          }
        `))),ca("error",Hr.css`
        :host([appearance='error'][disabled]),
        :host([appearance='error'][disabled]:hover),
        :host([appearance='error'][disabled]:active) {
          background: ${cr};
        }

        ${ua}
      `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
          :host([appearance='error'][disabled]) .control,
          :host([appearance='error'][disabled]) .control:hover {
            background: ${jr.ButtonFace};
            border-color: ${jr.GrayText};
            color: ${jr.GrayText};
          }
        `))),ca("lightweight",Hr.css`
        :host([appearance='lightweight'][disabled]:hover),
        :host([appearance='lightweight'][disabled]:active) {
          background-color: transparent;
          color: ${Qt};
        }

        :host([appearance='lightweight'][disabled]) .content::before,
        :host([appearance='lightweight'][disabled]:hover) .content::before,
        :host([appearance='lightweight'][disabled]:active) .content::before {
          background: transparent;
        }

        ${pa}
      `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
          :host([appearance='lightweight'].disabled) .control {
            forced-color-adjust: none;
            color: ${jr.GrayText};
          }

          :host([appearance='lightweight'].disabled)
            .control:hover
            .content::before {
            background: none;
          }
        `))),ca("outline",Hr.css`
        :host([appearance='outline'][disabled]),
        :host([appearance='outline'][disabled]:hover),
        :host([appearance='outline'][disabled]:active) {
          background: transparent;
          border-color: ${Rt};
        }

        ${ga}
      `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
          :host([appearance='outline'][disabled]) .control {
            border-color: ${jr.GrayText};
          }
        `))),ca("stealth",Hr.css`
        :host([appearance='stealth'][disabled]),
        :host([appearance='stealth'][disabled]:hover),
        :host([appearance='stealth'][disabled]:active) {
          background: ${bo};
        }

        ${ba}
      `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
          :host([appearance='stealth'][disabled]) {
            background: ${jr.ButtonFace};
          }

          :host([appearance='stealth'][disabled]) .control {
            background: ${jr.ButtonFace};
            border-color: transparent;
            color: ${jr.GrayText};
          }
        `)))),shadowOptions:{delegatesFocus:!0}}),xa="box-shadow: 0 0 calc((var(--elevation) * 0.225px) + 2px) rgba(0, 0, 0, calc(.11 * (2 - var(--background-luminance, 1)))), 0 calc(var(--elevation) * 0.4px) calc((var(--elevation) * 0.9px)) rgba(0, 0, 0, calc(.13 * (2 - var(--background-luminance, 1))));",ma=(e,t)=>Br.css`
        ${(0,ae.display)("block")} :host {
            --elevation: 4;
            display: block;
            contain: content;
            height: var(--card-height, 100%);
            width: var(--card-width, 100%);
            box-sizing: border-box;
            background: ${Lt};
            border-radius: calc(${$e} * 1px);
            ${xa}
        }
    `.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
                :host {
                    forced-color-adjust: none;
                    background: ${Ar.Canvas};
                    box-shadow: 0 0 0 1px ${Ar.CanvasText};
                }
            `));class va extends ae.Card{connectedCallback(){super.connectedCallback();const e=(0,ae.composedParent)(this);e&&Lt.setValueFor(this,(t=>Fo.getValueFor(t).evaluate(t,Lt.getValueFor(e))))}}va.compose({baseName:"card",baseClass:ae.Card,template:ae.cardTemplate,styles:ma});const ya=va.compose({baseName:"card",baseClass:rr.Card,template:rr.cardTemplate,styles:ma}),wa=(e,t)=>Hr.css`
    ${(0,rr.display)("inline-flex")} :host {
      align-items: center;
      outline: none;
      margin: calc(${me} * 1px) 0;
      /* Chromium likes to select label text or the default slot when the checkbox is
            clicked. Maybe there is a better solution here? */
      user-select: none;
    }

    .control {
      position: relative;
      width: calc((${Lr} / 2 + ${me}) * 1px);
      height: calc((${Lr} / 2 + ${me}) * 1px);
      box-sizing: border-box;
      border-radius: calc(${$e} * 1px);
      border: calc(${we} * 1px) solid ${Oo};
      background: ${co};
      outline: none;
      cursor: pointer;
    }

    .label {
      font-family: ${pe};
      color: ${Ho};
      /* Need to discuss with Brian how HorizontalSpacingNumber can work.
            https://github.com/microsoft/fast/issues/2766 */
      padding-inline-start: calc(${me} * 2px + 2px);
      margin-inline-end: calc(${me} * 2px + 2px);
      cursor: pointer;
      font-size: ${Fe};
      line-height: ${Te};
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    .checked-indicator {
      width: 100%;
      height: 100%;
      display: block;
      fill: ${_t};
      opacity: 0;
      pointer-events: none;
    }

    .indeterminate-indicator {
      border-radius: calc(${$e} * 1px);
      background: ${_t};
      position: absolute;
      top: 50%;
      left: 50%;
      width: 50%;
      height: 50%;
      transform: translate(-50%, -50%);
      opacity: 0;
    }

    :host(:not([disabled])) .control:hover {
      background: ${ho};
      border-color: ${No};
    }

    :host(:not([disabled])) .control:active {
      background: ${uo};
      border-color: ${Ro};
    }

    :host(:${rr.focusVisible}) .control {
      outline: calc(${ke} * 1px) solid ${Mt};
      outline-offset: 2px;
    }

    :host([aria-checked='true']) .control {
      background: ${Rt};
      border: calc(${we} * 1px) solid ${Rt};
    }

    :host([aria-checked='true']:not([disabled])) .control:hover {
      background: ${At};
      border: calc(${we} * 1px) solid ${At};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:hover
      .checked-indicator {
      fill: ${Et};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:hover
      .indeterminate-indicator {
      background: ${Et};
    }

    :host([aria-checked='true']:not([disabled])) .control:active {
      background: ${It};
      border: calc(${we} * 1px) solid ${It};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:active
      .checked-indicator {
      fill: ${qt};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:active
      .indeterminate-indicator {
      background: ${qt};
    }

    :host([aria-checked="true"]:${rr.focusVisible}:not([disabled])) .control {
      outline: calc(${ke} * 1px) solid ${Mt};
      outline-offset: 2px;
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
      cursor: ${rr.disabledCursor};
    }

    :host([aria-checked='true']:not(.indeterminate)) .checked-indicator,
    :host(.indeterminate) .indeterminate-indicator {
      opacity: 1;
    }

    :host([disabled]) {
      opacity: ${ye};
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      .control {
        forced-color-adjust: none;
        border-color: ${jr.FieldText};
        background: ${jr.Field};
      }
      .checked-indicator {
        fill: ${jr.FieldText};
      }
      .indeterminate-indicator {
        background: ${jr.FieldText};
      }
      :host(:not([disabled])) .control:hover,
      .control:active {
        border-color: ${jr.Highlight};
        background: ${jr.Field};
      }
      :host(:${rr.focusVisible}) .control {
        outline: calc(${ke} * 1px) solid ${jr.FieldText};
        outline-offset: 2px;
      }
      :host([aria-checked="true"]:${rr.focusVisible}:not([disabled])) .control {
        outline: calc(${ke} * 1px) solid ${jr.FieldText};
        outline-offset: 2px;
      }
      :host([aria-checked='true']) .control {
        background: ${jr.Highlight};
        border-color: ${jr.Highlight};
      }
      :host([aria-checked='true']:not([disabled])) .control:hover,
      .control:active {
        border-color: ${jr.Highlight};
        background: ${jr.HighlightText};
      }
      :host([aria-checked='true']) .checked-indicator {
        fill: ${jr.HighlightText};
      }
      :host([aria-checked='true']:not([disabled]))
        .control:hover
        .checked-indicator {
        fill: ${jr.Highlight};
      }
      :host([aria-checked='true']) .indeterminate-indicator {
        background: ${jr.HighlightText};
      }
      :host([aria-checked='true']) .control:hover .indeterminate-indicator {
        background: ${jr.Highlight};
      }
      :host([disabled]) {
        opacity: 1;
      }
      :host([disabled]) .control {
        forced-color-adjust: none;
        border-color: ${jr.GrayText};
        background: ${jr.Field};
      }
      :host([disabled]) .indeterminate-indicator,
      :host([aria-checked='true'][disabled])
        .control:hover
        .indeterminate-indicator {
        forced-color-adjust: none;
        background: ${jr.GrayText};
      }
      :host([disabled]) .checked-indicator,
      :host([aria-checked='true'][disabled]) .control:hover .checked-indicator {
        forced-color-adjust: none;
        fill: ${jr.GrayText};
      }
    `)),ka=rr.Checkbox.compose({baseName:"checkbox",template:rr.checkboxTemplate,styles:wa,checkedIndicator:'\n    <svg\n      part="checked-indicator"\n      class="checked-indicator"\n      viewBox="0 0 20 20"\n      xmlns="http://www.w3.org/2000/svg"\n    >\n      <path\n        fill-rule="evenodd"\n        clip-rule="evenodd"\n        d="M8.143 12.6697L15.235 4.5L16.8 5.90363L8.23812 15.7667L3.80005 11.2556L5.27591 9.7555L8.143 12.6697Z"\n      />\n    </svg>\n    ',indeterminateIndicator:'\n        <div part="indeterminate-indicator" class="indeterminate-indicator"></div>\n    '}),Fa="box-shadow: 0 0 calc((var(--elevation) * 0.225px) + 2px) rgba(0, 0, 0, calc(.11 * (2 - var(--background-luminance, 1)))), 0 calc(var(--elevation) * 0.4px) calc((var(--elevation) * 0.9px)) rgba(0, 0, 0, calc(.13 * (2 - var(--background-luminance, 1))));",Ta=(e,t)=>Hr.css`
    ${(0,rr.display)("inline-flex")} :host {
      --elevation: 14;
      background: ${co};
      border-radius: calc(${$e} * 1px);
      border: calc(${we} * 1px) solid ${vo};
      box-sizing: border-box;
      color: ${Ho};
      font-family: ${pe};
      height: calc(${Lr} * 1px);
      position: relative;
      user-select: none;
      outline: none;
      vertical-align: top;
    }

    :host(:not([autowidth])) {
      min-width: 250px;
    }

    .listbox {
      ${Fa}
      background: ${Tt};
      border: calc(${we} * 1px) solid ${Oo};
      border-radius: calc(${$e} * 1px);
      box-sizing: border-box;
      display: inline-flex;
      flex-direction: column;
      left: 0;
      max-height: calc(var(--max-height) - (${Lr} * 1px));
      padding: calc(${me} * 1px) 0;
      overflow-y: auto;
      position: absolute;
      z-index: 1;
    }

    :host(:not([autowidth])) .listbox {
      width: 100%;
    }

    :host([autowidth]) ::slotted([role='option']),
    :host([autowidth]) ::slotted(option) {
      padding: 0 calc(1em + ${me} * 1.25px + 1px);
    }

    .listbox[hidden] {
      display: none;
    }

    .control {
      align-items: center;
      box-sizing: border-box;
      cursor: pointer;
      display: flex;
      font-size: ${Fe};
      font-family: inherit;
      line-height: ${Te};
      min-height: 100%;
      padding: 0 calc(${me} * 2.25px);
      width: 100%;
    }

    :host([minimal]) {
      --density: -4;
    }

    :host(:not([disabled]):hover) {
      background: ${ho};
      border-color: ${yo};
    }

    :host(:${rr.focusVisible}) {
      border-color: ${Mt};
      box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px)
        ${Mt};
    }

    :host([disabled]) {
      cursor: ${rr.disabledCursor};
      opacity: ${ye};
    }

    :host([disabled]) .control {
      cursor: ${rr.disabledCursor};
      user-select: none;
    }

    :host([disabled]:hover) {
      background: ${bo};
      color: ${Ho};
      fill: currentcolor;
    }

    :host(:not([disabled])) .control:active {
      background: ${uo};
      border-color: ${It};
      border-radius: calc(${$e} * 1px);
    }

    :host([open][position='above']) .listbox {
      border-bottom-left-radius: 0;
      border-bottom-right-radius: 0;
    }

    :host([open][position='below']) .listbox {
      border-top-left-radius: 0;
      border-top-right-radius: 0;
    }

    :host([open][position='above']) .listbox {
      border-bottom: 0;
      bottom: calc(${Lr} * 1px);
    }

    :host([open][position='below']) .listbox {
      border-top: 0;
      top: calc(${Lr} * 1px);
    }

    .selected-value {
      flex: 1 1 auto;
      font-family: inherit;
      text-align: start;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }

    .indicator {
      flex: 0 0 auto;
      margin-inline-start: 1em;
    }

    slot[name='listbox'] {
      display: none;
      width: 100%;
    }

    :host([open]) slot[name='listbox'] {
      display: flex;
      position: absolute;
      ${Fa}
    }

    .end {
      margin-inline-start: auto;
    }

    .start,
    .end,
    .indicator,
    .select-indicator,
    ::slotted(svg) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      fill: currentcolor;
      height: 1em;
      min-height: calc(${me} * 4px);
      min-width: calc(${me} * 4px);
      width: 1em;
    }

    ::slotted([role='option']),
    ::slotted(option) {
      flex: 0 0 auto;
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      :host(:not([disabled]):hover),
      :host(:not([disabled]):active) {
        border-color: ${jr.Highlight};
      }

      :host(:not([disabled]):${rr.focusVisible}) {
        background-color: ${jr.ButtonFace};
        box-shadow: 0 0 0 calc(${ke} * 1px)
          ${jr.Highlight};
        color: ${jr.ButtonText};
        fill: currentcolor;
        forced-color-adjust: none;
      }

      :host(:not([disabled]):${rr.focusVisible}) .listbox {
        background: ${jr.ButtonFace};
      }

      :host([disabled]) {
        border-color: ${jr.GrayText};
        background-color: ${jr.ButtonFace};
        color: ${jr.GrayText};
        fill: currentcolor;
        opacity: 1;
        forced-color-adjust: none;
      }

      :host([disabled]:hover) {
        background: ${jr.ButtonFace};
      }

      :host([disabled]) .control {
        color: ${jr.GrayText};
        border-color: ${jr.GrayText};
      }

      :host([disabled]) .control .select-indicator {
        fill: ${jr.GrayText};
      }

      :host(:${rr.focusVisible}) ::slotted([aria-selected="true"][role="option"]),
            :host(:${rr.focusVisible}) ::slotted(option[aria-selected="true"]),
            :host(:${rr.focusVisible}) ::slotted([aria-selected="true"][role="option"]:not([disabled])) {
        background: ${jr.Highlight};
        border-color: ${jr.ButtonText};
        box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px)
          ${jr.HighlightText};
        color: ${jr.HighlightText};
        fill: currentcolor;
      }

      .start,
      .end,
      .indicator,
      .select-indicator,
      ::slotted(svg) {
        color: ${jr.ButtonText};
        fill: currentcolor;
      }
    `)),Ca=(e,t)=>Hr.css`
  ${Ta(e,t)}

  :host(:empty) .listbox {
    display: none;
  }

  :host([disabled]) *,
  :host([disabled]) {
    cursor: ${rr.disabledCursor};
    user-select: none;
  }

  :host(:focus-within:not([disabled])) {
    border-color: ${Mt};
    box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px)
      ${Mt};
  }

  .selected-value {
    -webkit-appearance: none;
    background: transparent;
    border: none;
    color: inherit;
    font-size: ${Fe};
    line-height: ${Te};
    height: calc(100% - (${we} * 1px));
    margin: auto 0;
    width: 100%;
  }

  .selected-value:hover,
  .selected-value:${rr.focusVisible},
  .selected-value:disabled,
  .selected-value:active {
    outline: none;
  }
`;class Va extends rr.Combobox{connectedCallback(){super.connectedCallback(),this.setAutoWidth()}slottedOptionsChanged(e,t){super.slottedOptionsChanged(e,t),this.setAutoWidth()}autoWidthChanged(e,t){t?this.setAutoWidth():this.style.removeProperty("width")}setAutoWidth(){if(!this.autoWidth||!this.isConnected)return;let e=this.listbox.getBoundingClientRect().width;0===e&&this.listbox.hidden&&(Object.assign(this.listbox.style,{visibility:"hidden"}),this.listbox.removeAttribute("hidden"),e=this.listbox.getBoundingClientRect().width,this.listbox.setAttribute("hidden",""),this.listbox.style.removeProperty("visibility")),e>0&&Object.assign(this.style,{width:`${e}px`})}}(0,Ir.gn)([(0,Hr.attr)({attribute:"autowidth",mode:"boolean"})],Va.prototype,"autoWidth",void 0),(0,Ir.gn)([(0,Hr.attr)({attribute:"minimal",mode:"boolean"})],Va.prototype,"minimal",void 0);const Da=Va.compose({baseName:"combobox",baseClass:rr.Combobox,template:rr.comboboxTemplate,styles:Ca,shadowOptions:{delegatesFocus:!0},indicator:'\n    <svg\n      class="select-indicator"\n      part="select-indicator"\n      viewBox="0 0 12 7"\n      xmlns="http://www.w3.org/2000/svg"\n    >\n      <path\n        d="M11.85.65c.2.2.2.5 0 .7L6.4 6.84a.55.55 0 01-.78 0L.14 1.35a.5.5 0 11.71-.7L6 5.8 11.15.65c.2-.2.5-.2.7 0z"\n      />\n    </svg>\n    '}),Sa=(e,t)=>Br.css`
    :host {
        display: grid;
        padding: 1px 0;
        box-sizing: border-box;
        width: 100%;
        border-bottom: calc(${we} * 1px) solid ${Mo};
    }

    :host(.header) {
    }

    :host(.sticky-header) {
        background: ${ao};
        position: sticky;
        top: 0;
    }
`,Ba=(e,t)=>Br.css`
    :host {
        display: flex;
        position: relative;
        flex-direction: column;
    }
`,za=(e,t)=>Hr.css`
    :host {
      padding: calc(${me} * 1px) calc(${me} * 3px);
      color: ${Ho};
      box-sizing: border-box;
      font-family: ${pe};
      font-size: ${Fe};
      line-height: ${Te};
      border: transparent calc(${we} * 1px) solid;
      font-weight: 400;
      overflow: hidden;
      white-space: nowrap;
      border-radius: calc(${$e} * 1px);
    }

    :host(.column-header) {
      font-weight: 600;
    }

    :host(:${rr.focusVisible}) {
      outline: calc(${ke} * 1px) solid ${Mt};
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      :host {
        forced-color-adjust: none;
        border-color: transparent;
        background: ${jr.Field};
        color: ${jr.FieldText};
      }

      :host(:${rr.focusVisible}) {
        border-color: ${jr.FieldText};
        box-shadow: 0 0 0 2px inset ${jr.Field};
      }
    `)),ja=rr.DataGridCell.compose({baseName:"data-grid-cell",template:rr.dataGridCellTemplate,styles:za}),Ha=rr.DataGridRow.compose({baseName:"data-grid-row",template:rr.dataGridRowTemplate,styles:Sa}),La=rr.DataGrid.compose({baseName:"data-grid",template:rr.dataGridTemplate,styles:Ba});class Oa extends rr.FoundationElement{}class Na extends((0,rr.FormAssociated)(Oa)){constructor(){super(...arguments),this.proxy=document.createElement("input")}}const Ra={toView(e){if(null==e)return null;const t=new Date(e);return"Invalid Date"===t.toString()?null:`${t.getFullYear().toString().padStart(4,"0")}-${(t.getMonth()+1).toString().padStart(2,"0")}-${t.getDate().toString().padStart(2,"0")}`},fromView(e){if(null==e)return null;const t=new Date(e);return"Invalid Date"===t.toString()?null:t}},Aa="Invalid Date";class Ia extends Na{constructor(){super(...arguments),this.step=1,this.isUserInput=!1}readOnlyChanged(){this.proxy instanceof HTMLInputElement&&(this.proxy.readOnly=this.readOnly,this.validate())}autofocusChanged(){this.proxy instanceof HTMLInputElement&&(this.proxy.autofocus=this.autofocus,this.validate())}listChanged(){this.proxy instanceof HTMLInputElement&&(this.proxy.setAttribute("list",this.list),this.validate())}maxChanged(e,t){var o;this.max=t<(null!==(o=this.min)&&void 0!==o?o:t)?this.min:t,this.value=this.getValidValue(this.value)}minChanged(e,t){var o;this.min=t>(null!==(o=this.max)&&void 0!==o?o:t)?this.max:t,this.value=this.getValidValue(this.value)}get valueAsNumber(){return new Date(super.value).valueOf()}set valueAsNumber(e){this.value=new Date(e).toString()}get valueAsDate(){return new Date(super.value)}set valueAsDate(e){this.value=e.toString()}valueChanged(e,t){this.value=this.getValidValue(t),t===this.value&&(this.control&&!this.isUserInput&&(this.control.value=this.value),super.valueChanged(e,this.value),void 0===e||this.isUserInput||this.$emit("change"),this.isUserInput=!1)}getValidValue(e){var t,o;let r=new Date(e);return r.toString()===Aa?r="":(r=r>(null!==(t=this.max)&&void 0!==t?t:r)?this.max:r,r=r<(null!==(o=this.min)&&void 0!==o?o:r)?this.min:r,r=`${r.getFullYear().toString().padStart(4,"0")}-${(r.getMonth()+1).toString().padStart(2,"0")}-${r.getDate().toString().padStart(2,"0")}`),r}stepUp(){const e=864e5*this.step,t=new Date(this.value);this.value=new Date(t.toString()!==Aa?t.valueOf()+e:0).toString()}stepDown(){const e=864e5*this.step,t=new Date(this.value);this.value=new Date(t.toString()!==Aa?Math.max(t.valueOf()-e,0):0).toString()}connectedCallback(){super.connectedCallback(),this.validate(),this.control.value=this.value,this.autofocus&&Hr.DOM.queueUpdate((()=>{this.focus()})),this.appearance||(this.appearance="outline")}handleTextInput(){this.isUserInput=!0,this.value=this.control.value}handleChange(){this.$emit("change")}handleKeyDown(e){switch(e.key){case"ArrowUp":return this.stepUp(),!1;case"ArrowDown":return this.stepDown(),!1}return!0}handleBlur(){this.control.value=this.value}}(0,Ir.gn)([Hr.attr],Ia.prototype,"appearance",void 0),(0,Ir.gn)([(0,Hr.attr)({attribute:"readonly",mode:"boolean"})],Ia.prototype,"readOnly",void 0),(0,Ir.gn)([(0,Hr.attr)({mode:"boolean"})],Ia.prototype,"autofocus",void 0),(0,Ir.gn)([Hr.attr],Ia.prototype,"list",void 0),(0,Ir.gn)([(0,Hr.attr)({converter:Hr.nullableNumberConverter})],Ia.prototype,"step",void 0),(0,Ir.gn)([(0,Hr.attr)({converter:Ra})],Ia.prototype,"max",void 0),(0,Ir.gn)([(0,Hr.attr)({converter:Ra})],Ia.prototype,"min",void 0),(0,Ir.gn)([Hr.observable],Ia.prototype,"defaultSlottedNodes",void 0),(0,rr.applyMixins)(Ia,rr.StartEnd,rr.DelegatesARIATextbox);const Ma=Hr.css`
  ${(0,rr.display)("inline-block")} :host {
    font-family: ${pe};
    outline: none;
    user-select: none;
  }

  .root {
    box-sizing: border-box;
    position: relative;
    display: flex;
    flex-direction: row;
    color: ${Ho};
    background: ${co};
    border-radius: calc(${$e} * 1px);
    border: calc(${we} * 1px) solid ${vo};
    height: calc(${Lr} * 1px);
  }

  .control {
    -webkit-appearance: none;
    font: inherit;
    background: transparent;
    border: 0;
    color: inherit;
    height: calc(100% - 4px);
    width: 100%;
    margin-top: auto;
    margin-bottom: auto;
    border: none;
    padding: 0 calc(${me} * 2px + 1px);
    font-size: ${Fe};
    line-height: ${Te};
  }

  .control:hover,
  .control:${rr.focusVisible},
  .control:disabled,
  .control:active {
    outline: none;
  }

  .label {
    display: block;
    color: ${Ho};
    cursor: pointer;
    font-size: ${Fe};
    line-height: ${Te};
    margin-bottom: 4px;
  }

  .label__hidden {
    display: none;
    visibility: hidden;
  }

  .start,
  .end {
    margin: auto;
    fill: currentcolor;
  }

  ::slotted(svg) {
    /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
    width: 16px;
    height: 16px;
  }

  .start {
    margin-inline-start: 11px;
  }

  .end {
    margin-inline-end: 11px;
  }

  :host(:hover:not([disabled])) .root {
    background: ${ho};
    border-color: ${yo};
  }

  :host(:active:not([disabled])) .root {
    background: ${ho};
    border-color: ${wo};
  }

  :host(:focus-within:not([disabled])) .root {
    border-color: ${Mt};
    box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px)
      ${Mt};
  }

  :host([appearance='filled']) .root {
    background: ${ao};
  }

  :host([appearance='filled']:hover:not([disabled])) .root {
    background: ${io};
  }

  :host([disabled]) .label,
  :host([readonly]) .label,
  :host([readonly]) .control,
  :host([disabled]) .control {
    cursor: ${rr.disabledCursor};
  }

  :host([disabled]) {
    opacity: ${ye};
  }

  :host([disabled]) .control {
    border-color: ${Oo};
  }
`.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
    .root,
    :host([appearance='filled']) .root {
      forced-color-adjust: none;
      background: ${jr.Field};
      border-color: ${jr.FieldText};
    }
    :host(:hover:not([disabled])) .root,
    :host([appearance='filled']:hover:not([disabled])) .root,
    :host([appearance='filled']:hover) .root {
      background: ${jr.Field};
      border-color: ${jr.Highlight};
    }
    .start,
    .end {
      fill: currentcolor;
    }
    :host([disabled]) {
      opacity: 1;
    }
    :host([disabled]) .root,
    :host([appearance='filled']:hover[disabled]) .root {
      border-color: ${jr.GrayText};
      background: ${jr.Field};
    }
    :host(:focus-within:enabled) .root {
      border-color: ${jr.Highlight};
      box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px)
        ${jr.Highlight};
    }
    input::placeholder {
      color: ${jr.GrayText};
    }
  `)),Pa=(e,t)=>Hr.css`
  ${Ma}
`,Ga=(e,t)=>Hr.html`
  <template class="${e=>e.readOnly?"readonly":""}">
    <label
      part="label"
      for="control"
      class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
    >
      <slot
        ${(0,Hr.slotted)({property:"defaultSlottedNodes",filter:rr.whitespaceFilter})}
      ></slot>
    </label>
    <div class="root" part="root">
      ${(0,rr.startSlotTemplate)(e,t)}
      <input
        class="control"
        part="control"
        id="control"
        @input="${e=>e.handleTextInput()}"
        @change="${e=>e.handleChange()}"
        ?autofocus="${e=>e.autofocus}"
        ?disabled="${e=>e.disabled}"
        list="${e=>e.list}"
        ?readonly="${e=>e.readOnly}"
        ?required="${e=>e.required}"
        :value="${e=>e.value}"
        type="date"
        aria-atomic="${e=>e.ariaAtomic}"
        aria-busy="${e=>e.ariaBusy}"
        aria-controls="${e=>e.ariaControls}"
        aria-current="${e=>e.ariaCurrent}"
        aria-describedby="${e=>e.ariaDescribedby}"
        aria-details="${e=>e.ariaDetails}"
        aria-disabled="${e=>e.ariaDisabled}"
        aria-errormessage="${e=>e.ariaErrormessage}"
        aria-flowto="${e=>e.ariaFlowto}"
        aria-haspopup="${e=>e.ariaHaspopup}"
        aria-hidden="${e=>e.ariaHidden}"
        aria-invalid="${e=>e.ariaInvalid}"
        aria-keyshortcuts="${e=>e.ariaKeyshortcuts}"
        aria-label="${e=>e.ariaLabel}"
        aria-labelledby="${e=>e.ariaLabelledby}"
        aria-live="${e=>e.ariaLive}"
        aria-owns="${e=>e.ariaOwns}"
        aria-relevant="${e=>e.ariaRelevant}"
        aria-roledescription="${e=>e.ariaRoledescription}"
        ${(0,Hr.ref)("control")}
      />
      ${(0,rr.endSlotTemplate)(e,t)}
    </div>
  </template>
`,_a=Ia.compose({baseName:"date-field",styles:Pa,template:Ga,shadowOptions:{delegatesFocus:!0}}),Ea=(e,t)=>Br.css`
    :host([hidden]) {
        display: none;
    }

    :host {
        --elevation: 14;
        --dialog-height: 480px;
        --dialog-width: 640px;
        display: block;
    }

    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.3);
        touch-action: none;
    }

    .positioning-region {
        display: flex;
        justify-content: center;
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        overflow: auto;
    }

    .control {
        ${xa}
        margin-top: auto;
        margin-bottom: auto;
        width: var(--dialog-width);
        height: var(--dialog-height);
        background-color: ${Lt};
        z-index: 1;
        border-radius: calc(${$e} * 1px);
        border: calc(${we} * 1px) solid transparent;
    }
`,qa=rr.Dialog.compose({baseName:"dialog",template:rr.dialogTemplate,styles:Ea}),Wa=(e,t)=>Br.css`
        ${(0,ae.display)("block")} :host {
            box-sizing: content-box;
            height: 0;
            margin: calc(${me} * 1px) 0;
            border-top: calc(${we} * 1px) solid ${Mo};
            border-left: none;
        }

        :host([orientation="vertical"]) {
            height: 100%;
            margin: 0 calc(${me} * 1px);
            border-top: none;
            border-left: calc(${we} * 1px) solid ${Mo};
        }
    `,Ua=rr.Divider.compose({baseName:"divider",template:rr.dividerTemplate,styles:Wa}),Xa=(e,t)=>{const o=e.tagFor(rr.ListboxOption),r=e.name===e.tagFor(rr.ListboxElement)?"":".listbox";return Hr.css`
        ${r?"":(0,rr.display)("inline-flex")}

        :host ${r} {
            background: ${Lt};
            border: calc(${we} * 1px) solid ${Oo};
            border-radius: calc(${$e} * 1px);
            box-sizing: border-box;
            flex-direction: column;
            padding: calc(${me} * 1px) 0;
        }

        ${r?"":Hr.css`
            :host(:${rr.focusVisible}:not([disabled])) {
                outline: none;
            }

            :host(:focus-within:not([disabled])) {
                border-color: ${Vo};
                box-shadow: 0 0 0
                    calc((${ke} - ${we}) * 1px)
                    ${Vo} inset;
            }

            :host([disabled]) ::slotted(*) {
                cursor: ${rr.disabledCursor};
                opacity: ${ye};
                pointer-events: none;
            }
        `}

        ${r||":host([size])"} {
            max-height: calc(
                (var(--size) * ${Lr} + (${me} * ${we} * 2)) * 1px
            );
            overflow-y: auto;
        }

        :host([size="0"]) ${r} {
            max-height: none;
        }
    `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
                :host(:not([multiple]):${rr.focusVisible}) ::slotted(${o}[aria-selected="true"]),
                :host([multiple]:${rr.focusVisible}) ::slotted(${o}[aria-checked="true"]) {
                    border-color: ${jr.ButtonText};
                    box-shadow: 0 0 0 calc(${ke} * 1px) inset ${jr.HighlightText};
                }

                :host(:not([multiple]):${rr.focusVisible}) ::slotted(${o}[aria-selected="true"]) {
                    background: ${jr.Highlight};
                    color: ${jr.HighlightText};
                    fill: currentcolor;
                }

                ::slotted(${o}[aria-selected="true"]:not([aria-checked="true"])) {
                    background: ${jr.Highlight};
                    border-color: ${jr.HighlightText};
                    color: ${jr.HighlightText};
                }
            `))},Za=rr.ListboxElement.compose({baseName:"listbox",template:rr.listboxTemplate,styles:Xa}),Ya=(e,t)=>Br.css`
        ${(0,ae.display)("block")} :host {
            --elevation: 11;
            background: ${Lt};
            border: calc(${we} * 1px) solid transparent;
            ${xa}
            margin: 0;
            border-radius: calc(${$e} * 1px);
            padding: calc(${me} * 1px) 0;
            max-width: 368px;
            min-width: 64px;
        }

        :host([slot="submenu"]) {
            width: max-content;
            margin: 0 calc(${me} * 1px);
        }

        ::slotted(hr) {
            box-sizing: content-box;
            height: 0;
            margin: 0;
            border: none;
            border-top: calc(${we} * 1px) solid ${Mo};
        }
    `.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
                :host {
                    background: ${Ar.Canvas};
                    border-color: ${Ar.CanvasText};
                }
            `)),Ja=rr.Menu.compose({baseName:"menu",template:rr.menuTemplate,styles:Ya}),Ka=(e,t)=>Hr.css`
    ${(0,rr.display)("grid")} :host {
      contain: layout;
      overflow: visible;
      font-family: ${pe};
      outline: none;
      box-sizing: border-box;
      height: calc(${Lr} * 1px);
      grid-template-columns: minmax(42px, auto) 1fr minmax(42px, auto);
      grid-template-rows: auto;
      justify-items: center;
      align-items: center;
      padding: 0;
      margin: 0 calc(${me} * 1px);
      white-space: nowrap;
      color: ${Ho};
      fill: currentcolor;
      cursor: pointer;
      font-size: ${Fe};
      line-height: ${Te};
      border-radius: calc(${$e} * 1px);
      border: calc(${ke} * 1px) solid transparent;
    }

    :host(:hover) {
      position: relative;
      z-index: 1;
    }

    :host(.indent-0) {
      grid-template-columns: auto 1fr minmax(42px, auto);
    }
    :host(.indent-0) .content {
      grid-column: 1;
      grid-row: 1;
      margin-inline-start: 10px;
    }
    :host(.indent-0) .expand-collapse-glyph-container {
      grid-column: 5;
      grid-row: 1;
    }
    :host(.indent-2) {
      grid-template-columns:
        minmax(42px, auto) minmax(42px, auto) 1fr minmax(42px, auto)
        minmax(42px, auto);
    }
    :host(.indent-2) .content {
      grid-column: 3;
      grid-row: 1;
      margin-inline-start: 10px;
    }
    :host(.indent-2) .expand-collapse-glyph-container {
      grid-column: 5;
      grid-row: 1;
    }
    :host(.indent-2) .start {
      grid-column: 2;
    }
    :host(.indent-2) .end {
      grid-column: 4;
    }

    :host(:${rr.focusVisible}) {
      border-color: ${Vo};
      background: ${zt};
      color: ${Ho};
    }

    :host(:hover) {
      background: ${zt};
      color: ${Ho};
    }

    :host([aria-checked='true']),
    :host(:active),
    :host(.expanded) {
      background: ${St};
      color: ${Ho};
    }

    :host([disabled]) {
      cursor: ${rr.disabledCursor};
      opacity: ${ye};
    }

    :host([disabled]:hover) {
      color: ${Ho};
      fill: currentcolor;
      background: ${bo};
    }

    :host([disabled]:hover) .start,
    :host([disabled]:hover) .end,
    :host([disabled]:hover)::slotted(svg) {
      fill: ${Ho};
    }

    .expand-collapse-glyph {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;
      fill: currentcolor;
    }

    .content {
      grid-column-start: 2;
      justify-self: start;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .start,
    .end {
      display: flex;
      justify-content: center;
    }

    ::slotted(svg) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;
    }

    :host(:hover) .start,
    :host(:hover) .end,
    :host(:hover)::slotted(svg),
    :host(:active) .start,
    :host(:active) .end,
    :host(:active)::slotted(svg) {
      fill: ${Ho};
    }

    :host(.indent-0[aria-haspopup='menu']) {
      display: grid;
      grid-template-columns: minmax(42px, auto) auto 1fr minmax(42px, auto) minmax(
          42px,
          auto
        );
      align-items: center;
      min-height: 32px;
    }

    :host(.indent-1[aria-haspopup='menu']),
    :host(.indent-1[role='menuitemcheckbox']),
    :host(.indent-1[role='menuitemradio']) {
      display: grid;
      grid-template-columns: minmax(42px, auto) auto 1fr minmax(42px, auto) minmax(
          42px,
          auto
        );
      align-items: center;
      min-height: 32px;
    }

    :host(.indent-2:not([aria-haspopup='menu'])) .end {
      grid-column: 5;
    }

    :host .input-container,
    :host .expand-collapse-glyph-container {
      display: none;
    }

    :host([aria-haspopup='menu']) .expand-collapse-glyph-container,
    :host([role='menuitemcheckbox']) .input-container,
    :host([role='menuitemradio']) .input-container {
      display: grid;
      margin-inline-end: 10px;
    }

    :host([aria-haspopup='menu']) .content,
    :host([role='menuitemcheckbox']) .content,
    :host([role='menuitemradio']) .content {
      grid-column-start: 3;
    }

    :host([aria-haspopup='menu'].indent-0) .content {
      grid-column-start: 1;
    }

    :host([aria-haspopup='menu']) .end,
    :host([role='menuitemcheckbox']) .end,
    :host([role='menuitemradio']) .end {
      grid-column-start: 4;
    }

    :host .expand-collapse,
    :host .checkbox,
    :host .radio {
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      width: 20px;
      height: 20px;
      box-sizing: border-box;
      outline: none;
      margin-inline-start: 10px;
    }

    :host .checkbox,
    :host .radio {
      border: calc(${we} * 1px) solid ${Ho};
    }

    :host([aria-checked='true']) .checkbox,
    :host([aria-checked='true']) .radio {
      background: ${Rt};
      border-color: ${Rt};
    }

    :host .checkbox {
      border-radius: calc(${$e} * 1px);
    }

    :host .radio {
      border-radius: 999px;
    }

    :host .checkbox-indicator,
    :host .radio-indicator,
    :host .expand-collapse-indicator,
    ::slotted([slot='checkbox-indicator']),
    ::slotted([slot='radio-indicator']),
    ::slotted([slot='expand-collapse-indicator']) {
      display: none;
    }

    ::slotted([slot='end']:not(svg)) {
      margin-inline-end: 10px;
      color: ${zo};
    }

    :host([aria-checked='true']) .checkbox-indicator,
    :host([aria-checked='true']) ::slotted([slot='checkbox-indicator']) {
      width: 100%;
      height: 100%;
      display: block;
      fill: ${_t};
      pointer-events: none;
    }

    :host([aria-checked='true']) .radio-indicator {
      position: absolute;
      top: 4px;
      left: 4px;
      right: 4px;
      bottom: 4px;
      border-radius: 999px;
      display: block;
      background: ${_t};
      pointer-events: none;
    }

    :host([aria-checked='true']) ::slotted([slot='radio-indicator']) {
      display: block;
      pointer-events: none;
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      :host {
        border-color: transparent;
        color: ${jr.ButtonText};
        forced-color-adjust: none;
      }

      :host(:hover) {
        background: ${jr.Highlight};
        color: ${jr.HighlightText};
      }

      :host(:hover) .start,
      :host(:hover) .end,
      :host(:hover)::slotted(svg),
      :host(:active) .start,
      :host(:active) .end,
      :host(:active)::slotted(svg) {
        fill: ${jr.HighlightText};
      }

      :host(.expanded) {
        background: ${jr.Highlight};
        border-color: ${jr.Highlight};
        color: ${jr.HighlightText};
      }

      :host(:${rr.focusVisible}) {
        background: ${jr.Highlight};
        border-color: ${jr.ButtonText};
        box-shadow: 0 0 0 calc(${ke} * 1px) inset
          ${jr.HighlightText};
        color: ${jr.HighlightText};
        fill: currentcolor;
      }

      :host([disabled]),
      :host([disabled]:hover),
      :host([disabled]:hover) .start,
      :host([disabled]:hover) .end,
      :host([disabled]:hover)::slotted(svg) {
        background: ${jr.Canvas};
        color: ${jr.GrayText};
        fill: currentcolor;
        opacity: 1;
      }

      :host .expanded-toggle,
      :host .checkbox,
      :host .radio {
        border-color: ${jr.ButtonText};
        background: ${jr.HighlightText};
      }

      :host([checked='true']) .checkbox,
      :host([checked='true']) .radio {
        background: ${jr.HighlightText};
        border-color: ${jr.HighlightText};
      }

      :host(:hover) .expanded-toggle,
            :host(:hover) .checkbox,
            :host(:hover) .radio,
            :host(:${rr.focusVisible}) .expanded-toggle,
            :host(:${rr.focusVisible}) .checkbox,
            :host(:${rr.focusVisible}) .radio,
            :host([checked="true"]:hover) .checkbox,
            :host([checked="true"]:hover) .radio,
            :host([checked="true"]:${rr.focusVisible}) .checkbox,
            :host([checked="true"]:${rr.focusVisible}) .radio {
        border-color: ${jr.HighlightText};
      }

      :host([aria-checked='true']) {
        background: ${jr.Highlight};
        color: ${jr.HighlightText};
      }

      :host([aria-checked='true']) .checkbox-indicator,
      :host([aria-checked='true']) ::slotted([slot='checkbox-indicator']),
      :host([aria-checked='true']) ::slotted([slot='radio-indicator']) {
        fill: ${jr.Highlight};
      }

      :host([aria-checked='true']) .radio-indicator {
        background: ${jr.Highlight};
      }

      ::slotted([slot='end']:not(svg)) {
        color: ${jr.ButtonText};
      }

      :host(:hover) ::slotted([slot="end"]:not(svg)),
            :host(:${rr.focusVisible}) ::slotted([slot="end"]:not(svg)) {
        color: ${jr.HighlightText};
      }
    `),new ar(Hr.css`
        .expand-collapse-glyph {
          transform: rotate(0deg);
        }
      `,Hr.css`
        .expand-collapse-glyph {
          transform: rotate(180deg);
        }
      `)),Qa=rr.MenuItem.compose({baseName:"menu-item",template:rr.menuItemTemplate,styles:Ka,checkboxIndicator:'\n      <svg\n        part="checkbox-indicator"\n        class="checkbox-indicator"\n        viewBox="0 0 20 20"\n        xmlns="http://www.w3.org/2000/svg"\n      >\n        <path\n          fill-rule="evenodd"\n          clip-rule="evenodd"\n          d="M8.143 12.6697L15.235 4.5L16.8 5.90363L8.23812 15.7667L3.80005 11.2556L5.27591 9.7555L8.143 12.6697Z"\n        />\n      </svg>\n    ',expandCollapseGlyph:'\n      <svg\n        viewBox="0 0 16 16"\n        xmlns="http://www.w3.org/2000/svg"\n        class="expand-collapse-glyph"\n        part="expand-collapse-glyph"\n      >\n        <path\n          d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"\n        />\n      </svg>\n    ',radioIndicator:'\n      <span part="radio-indicator" class="radio-indicator"></span>\n    '});class ei extends ae.NumberField{constructor(){super(...arguments),this.appearance="outline"}}(0,Ir.gn)([Br.attr],ei.prototype,"appearance",void 0),ei.compose({baseName:"number-field",baseClass:ae.NumberField,styles:(e,t)=>Br.css`
    ${(0,ae.display)("inline-block")} :host {
        font-family: ${pe};
        outline: none;
        user-select: none;
    }

    .root {
        box-sizing: border-box;
        position: relative;
        display: flex;
        flex-direction: row;
        color: ${Ho};
        background: ${co};
        border-radius: calc(${$e} * 1px);
        border: calc(${we} * 1px) solid ${Rt};
        height: calc(${Mr} * 1px);
        align-items: baseline;
    }

    .control {
        -webkit-appearance: none;
        font: inherit;
        background: transparent;
        border: 0;
        color: inherit;
        height: calc(100% - 4px);
        width: 100%;
        margin-top: auto;
        margin-bottom: auto;
        border: none;
        padding: 0 calc(${me} * 2px + 1px);
        font-size: ${Fe};
        line-height: ${Te};
    }

    .control:hover,
    .control:${ae.focusVisible},
    .control:disabled,
    .control:active {
        outline: none;
    }

    .controls {
        opacity: 0;
    }

    .label {
        display: block;
        color: ${Ho};
        cursor: pointer;
        font-size: ${Fe};
        line-height: ${Te};
        margin-bottom: 4px;
    }

    .label__hidden {
        display: none;
        visibility: hidden;
    }

    .start,
    .control,
    .controls,
    .end {
        align-self: center;
    }

    .start,
    .end {
        margin: auto;
        fill: currentcolor;
    }

    .step-up-glyph,
    .step-down-glyph {
        display: block;
        padding: 4px 10px;
        cursor: pointer;
    }

    .step-up-glyph:before,
    .step-down-glyph:before {
        content: '';
        display: block;
        border: solid transparent 6px;
    }

    .step-up-glyph:before {
        border-bottom-color: ${Ho};
    }

    .step-down-glyph:before {
        border-top-color: ${Ho};
    }

    ::slotted(svg) {
        /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
        width: 16px;
        height: 16px;
    }

    .start {
        margin-inline-start: 11px;
    }

    .end {
        margin-inline-end: 11px;
    }

    :host(:hover:not([disabled])) .root {
        background: ${ho};
        border-color: ${At};
    }

    :host(:active:not([disabled])) .root {
        background: ${ho};
        border-color: ${It};
    }

    :host(:focus-within:not([disabled])) .root {
        border-color: ${Vo};
        box-shadow: 0 0 0 calc(${ke} * 1px) ${Vo} inset;
    }

    :host(:hover:not([disabled])) .controls,
    :host(:focus-within:not([disabled])) .controls {
        opacity: 1;
    }

    :host([appearance="filled"]) .root {
        background: ${ao};
    }

    :host([appearance="filled"]:hover:not([disabled])) .root {
        background: ${io};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
        cursor: ${ae.disabledCursor};
    }

    :host([disabled]) {
        opacity: ${ye};
    }

    :host([disabled]) .control {
        border-color: ${Oo};
    }
`.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
                .root,
                :host([appearance="filled"]) .root {
                    forced-color-adjust: none;
                    background: ${Ar.Field};
                    border-color: ${Ar.FieldText};
                }
                :host(:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover) .root {
                    background: ${Ar.Field};
                    border-color: ${Ar.Highlight};
                }
                .start,
                .end {
                    fill: currentcolor;
                }
                :host([disabled]) {
                    opacity: 1;
                }
                :host([disabled]) .root,
                :host([appearance="filled"]:hover[disabled]) .root {
                    border-color: ${Ar.GrayText};
                    background: ${Ar.Field};
                }
                :host(:focus-within:enabled) .root {
                    border-color: ${Ar.Highlight};
                    box-shadow: 0 0 0 1px ${Ar.Highlight} inset;
                }
                input::placeholder {
                    color: ${Ar.GrayText};
                }
            `)),template:ae.numberFieldTemplate,shadowOptions:{delegatesFocus:!0},stepDownGlyph:'\n        <span class="step-down-glyph" part="step-down-glyph"></span>\n    ',stepUpGlyph:'\n        <span class="step-up-glyph" part="step-up-glyph"></span>\n    '});const ti=(e,t)=>Hr.css`
  ${Ma}

  .controls {
    opacity: 0;
  }

  .step-up-glyph,
  .step-down-glyph {
    display: block;
    padding: 4px 10px;
    cursor: pointer;
  }

  .step-up-glyph:before,
  .step-down-glyph:before {
    content: '';
    display: block;
    border: solid transparent 6px;
  }

  .step-up-glyph:before {
    border-bottom-color: ${Ho};
  }

  .step-down-glyph:before {
    border-top-color: ${Ho};
  }

  :host(:hover:not([disabled])) .controls,
  :host(:focus-within:not([disabled])) .controls {
    opacity: 1;
  }
`,oi=ei.compose({baseName:"number-field",baseClass:rr.NumberField,styles:ti,template:rr.numberFieldTemplate,shadowOptions:{delegatesFocus:!0},stepDownGlyph:'\n        <span class="step-down-glyph" part="step-down-glyph"></span>\n    ',stepUpGlyph:'\n        <span class="step-up-glyph" part="step-up-glyph"></span>\n    '}),ri=(e,t)=>Hr.css`
    ${(0,rr.display)("inline-flex")} :host {
      align-items: center;
      font-family: ${pe};
      border-radius: calc(${$e} * 1px);
      border: calc(${ke} * 1px) solid transparent;
      box-sizing: border-box;
      color: ${Ho};
      cursor: pointer;
      flex: 0 0 auto;
      fill: currentcolor;
      font-size: ${Fe};
      height: calc(${Lr} * 1px);
      line-height: ${Te};
      margin: 0 calc(${me} * 1px);
      outline: none;
      overflow: hidden;
      padding: 0 calc(${me} * 2.25px);
      user-select: none;
      white-space: nowrap;
    }

    /* TODO should we use outline instead of background for focus to support multi-selection */
    :host(:${rr.focusVisible}) {
      background: ${Mt};
      color: ${Wt};
    }

    :host([aria-selected='true']) {
      background: ${Rt};
      color: ${_t};
    }

    :host(:hover) {
      background: ${At};
      color: ${Et};
    }

    :host(:active) {
      background: ${It};
      color: ${qt};
    }

    :host(:not([aria-selected='true']):hover),
    :host(:not([aria-selected='true']):active) {
      background: ${io};
      color: ${Ho};
    }

    :host([disabled]) {
      cursor: ${rr.disabledCursor};
      opacity: ${ye};
    }

    :host([disabled]:hover) {
      background-color: inherit;
    }

    .content {
      grid-column-start: 2;
      justify-self: start;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .start,
    .end,
    ::slotted(svg) {
      display: flex;
    }

    ::slotted(svg) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      height: calc(${me} * 4px);
      width: calc(${me} * 4px);
    }

    ::slotted([slot='end']) {
      margin-inline-start: 1ch;
    }

    ::slotted([slot='start']) {
      margin-inline-end: 1ch;
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      :host {
        border-color: transparent;
        forced-color-adjust: none;
        color: ${jr.ButtonText};
        fill: currentcolor;
      }

      :host(:not([aria-selected='true']):hover),
      :host([aria-selected='true']) {
        background: ${jr.Highlight};
        color: ${jr.HighlightText};
      }

      :host([disabled]),
      :host([disabled]:not([aria-selected='true']):hover) {
        background: ${jr.Canvas};
        color: ${jr.GrayText};
        fill: currentcolor;
        opacity: 1;
      }
    `)),ai=rr.ListboxOption.compose({baseName:"option",template:rr.listboxOptionTemplate,styles:ri}),ii=(e,t)=>Br.css`
        ${(0,ae.display)("flex")} :host {
            align-items: center;
            outline: none;
            height: calc(${me} * 1px);
            margin: calc(${me} * 1px) 0;
        }

        .progress {
            background-color: ${ao};
            border-radius: calc(${me} * 1px);
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            position: relative;
        }

        .determinate {
            background-color: ${Qt};
            border-radius: calc(${me} * 1px);
            height: 100%;
            transition: all 0.2s ease-in-out;
            display: flex;
        }

        .indeterminate {
            height: 100%;
            border-radius: calc(${me} * 1px);
            display: flex;
            width: 100%;
            position: relative;
            overflow: hidden;
        }

        .indeterminate-indicator-1 {
            position: absolute;
            opacity: 0;
            height: 100%;
            background-color: ${Qt};
            border-radius: calc(${me} * 1px);
            animation-timing-function: cubic-bezier(0.4, 0, 0.6, 1);
            width: 40%;
            animation: indeterminate-1 2s infinite;
        }

        .indeterminate-indicator-2 {
            position: absolute;
            opacity: 0;
            height: 100%;
            background-color: ${Qt};
            border-radius: calc(${me} * 1px);
            animation-timing-function: cubic-bezier(0.4, 0, 0.6, 1);
            width: 60%;
            animation: indeterminate-2 2s infinite;
        }

        :host([paused]) .indeterminate-indicator-1,
        :host([paused]) .indeterminate-indicator-2 {
            animation-play-state: paused;
            background-color: ${ao};
        }

        :host([paused]) .determinate {
            background-color: ${zo};
        }

        @keyframes indeterminate-1 {
            0% {
                opacity: 1;
                transform: translateX(-100%);
            }
            70% {
                opacity: 1;
                transform: translateX(300%);
            }
            70.01% {
                opacity: 0;
            }
            100% {
                opacity: 0;
                transform: translateX(300%);
            }
        }

        @keyframes indeterminate-2 {
            0% {
                opacity: 0;
                transform: translateX(-150%);
            }
            29.99% {
                opacity: 0;
            }
            30% {
                opacity: 1;
                transform: translateX(-150%);
            }
            100% {
                transform: translateX(166.66%);
                opacity: 1;
            }
        }
    `.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
                .progress {
                    forced-color-adjust: none;
                    background-color: ${Ar.Field};
                    box-shadow: 0 0 0 1px inset ${Ar.FieldText};
                }
                .determinate,
                .indeterminate-indicator-1,
                .indeterminate-indicator-2 {
                    forced-color-adjust: none;
                    background-color: ${Ar.FieldText};
                }
                :host([paused]) .determinate,
                :host([paused]) .indeterminate-indicator-1,
                :host([paused]) .indeterminate-indicator-2 {
                    background-color: ${Ar.GrayText};
                }
            `)),li=rr.BaseProgress.compose({baseName:"progress",template:rr.progressTemplate,styles:ii,indeterminateIndicator1:'\n        <span class="indeterminate-indicator-1" part="indeterminate-indicator-1"></span>\n    ',indeterminateIndicator2:'\n        <span class="indeterminate-indicator-2" part="indeterminate-indicator-2"></span>\n    '}),ni=rr.BaseProgress.compose({baseName:"progress-ring",template:rr.progressRingTemplate,styles:(e,t)=>Br.css`
        ${(0,ae.display)("flex")} :host {
            align-items: center;
            outline: none;
            height: calc(${Mr} * 1px);
            width: calc(${Mr} * 1px);
            margin: calc(${Mr} * 1px) 0;
        }

        .progress {
            height: 100%;
            width: 100%;
        }

        .background {
            stroke: ${ao};
            fill: none;
            stroke-width: 2px;
        }

        .determinate {
            stroke: ${Qt};
            fill: none;
            stroke-width: 2px;
            stroke-linecap: round;
            transform-origin: 50% 50%;
            transform: rotate(-90deg);
            transition: all 0.2s ease-in-out;
        }

        .indeterminate-indicator-1 {
            stroke: ${Qt};
            fill: none;
            stroke-width: 2px;
            stroke-linecap: round;
            transform-origin: 50% 50%;
            transform: rotate(-90deg);
            transition: all 0.2s ease-in-out;
            animation: spin-infinite 2s linear infinite;
        }

        :host([paused]) .indeterminate-indicator-1 {
            animation-play-state: paused;
            stroke: ${ao};
        }

        :host([paused]) .determinate {
            stroke: ${zo};
        }

        @keyframes spin-infinite {
            0% {
                stroke-dasharray: 0.01px 43.97px;
                transform: rotate(0deg);
            }
            50% {
                stroke-dasharray: 21.99px 21.99px;
                transform: rotate(450deg);
            }
            100% {
                stroke-dasharray: 0.01px 43.97px;
                transform: rotate(1080deg);
            }
        }
    `.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
                .indeterminate-indicator-1,
                .determinate {
                    stroke: ${Ar.FieldText};
                }
                .background {
                    stroke: ${Ar.Field};
                }
                :host([paused]) .indeterminate-indicator-1 {
                    stroke: ${Ar.Field};
                }
                :host([paused]) .determinate {
                    stroke: ${Ar.GrayText};
                }
            `)),indeterminateIndicator:'\n        <svg class="progress" part="progress" viewBox="0 0 16 16">\n            <circle\n                class="background"\n                part="background"\n                cx="8px"\n                cy="8px"\n                r="7px"\n            ></circle>\n            <circle\n                class="indeterminate-indicator-1"\n                part="indeterminate-indicator-1"\n                cx="8px"\n                cy="8px"\n                r="7px"\n            ></circle>\n        </svg>\n    '}),si=(e,t)=>Hr.css`
    ${(0,rr.display)("inline-flex")} :host {
      --input-size: calc((${Lr} / 2) + ${me});
      align-items: center;
      outline: none;
      margin: calc(${me} * 1px) 0;
      /* Chromium likes to select label text or the default slot when
         the radio is clicked. Maybe there is a better solution here? */
      user-select: none;
      position: relative;
      flex-direction: row;
      transition: all 0.2s ease-in-out;
    }

    .control {
      position: relative;
      width: calc((${Lr} / 2 + ${me}) * 1px);
      height: calc((${Lr} / 2 + ${me}) * 1px);
      box-sizing: border-box;
      border-radius: 999px;
      border: calc(${we} * 1px) solid ${Oo};
      background: ${co};
      outline: none;
      cursor: pointer;
    }

    .label {
      font-family: ${pe};
      color: ${Ho};
      /* Need to discuss with Brian how HorizontalSpacingNumber can work.
            https://github.com/microsoft/fast/issues/2766 */
      padding-inline-start: calc(${me} * 2px + 2px);
      margin-inline-end: calc(${me} * 2px + 2px);
      cursor: pointer;
      font-size: ${Fe};
      line-height: ${Te};
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    .control,
    .checked-indicator {
      flex-shrink: 0;
    }

    .checked-indicator {
      position: absolute;
      top: 5px;
      left: 5px;
      right: 5px;
      bottom: 5px;
      border-radius: 999px;
      display: inline-block;
      background: ${_t};
      fill: ${_t};
      opacity: 0;
      pointer-events: none;
    }

    :host(:not([disabled])) .control:hover {
      background: ${ho};
      border-color: ${No};
    }

    :host(:not([disabled])) .control:active {
      background: ${uo};
      border-color: ${Ro};
    }

    :host(:${rr.focusVisible}) .control {
      outline: solid calc(${ke} * 1px) ${Mt};
    }

    :host([aria-checked='true']) .control {
      background: ${Rt};
      border: calc(${we} * 1px) solid ${Rt};
    }

    :host([aria-checked='true']:not([disabled])) .control:hover {
      background: ${At};
      border: calc(${we} * 1px) solid ${At};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:hover
      .checked-indicator {
      background: ${Et};
      fill: ${Et};
    }

    :host([aria-checked='true']:not([disabled])) .control:active {
      background: ${It};
      border: calc(${we} * 1px) solid ${It};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:active
      .checked-indicator {
      background: ${qt};
      fill: ${qt};
    }

    :host([aria-checked="true"]:${rr.focusVisible}:not([disabled])) .control {
      outline-offset: 2px;
      outline: solid calc(${ke} * 1px) ${Mt};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
      cursor: ${rr.disabledCursor};
    }

    :host([aria-checked='true']) .checked-indicator {
      opacity: 1;
    }

    :host([disabled]) {
      opacity: ${ye};
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      .control,
      :host([aria-checked='true']:not([disabled])) .control {
        forced-color-adjust: none;
        border-color: ${jr.FieldText};
        background: ${jr.Field};
      }
      :host(:not([disabled])) .control:hover {
        border-color: ${jr.Highlight};
        background: ${jr.Field};
      }
      :host([aria-checked='true']:not([disabled])) .control:hover,
      :host([aria-checked='true']:not([disabled])) .control:active {
        border-color: ${jr.Highlight};
        background: ${jr.Highlight};
      }
      :host([aria-checked='true']) .checked-indicator {
        background: ${jr.Highlight};
        fill: ${jr.Highlight};
      }
      :host([aria-checked='true']:not([disabled]))
        .control:hover
        .checked-indicator,
      :host([aria-checked='true']:not([disabled]))
        .control:active
        .checked-indicator {
        background: ${jr.HighlightText};
        fill: ${jr.HighlightText};
      }
      :host(:${rr.focusVisible}) .control {
        border-color: ${jr.Highlight};
        outline-offset: 2px;
        outline: solid calc(${ke} * 1px) ${jr.FieldText};
      }
      :host([aria-checked="true"]:${rr.focusVisible}:not([disabled])) .control {
        border-color: ${jr.Highlight};
        outline: solid calc(${ke} * 1px) ${jr.FieldText};
      }
      :host([disabled]) {
        forced-color-adjust: none;
        opacity: 1;
      }
      :host([disabled]) .label {
        color: ${jr.GrayText};
      }
      :host([disabled]) .control,
      :host([aria-checked='true'][disabled]) .control:hover,
      .control:active {
        background: ${jr.Field};
        border-color: ${jr.GrayText};
      }
      :host([disabled]) .checked-indicator,
      :host([aria-checked='true'][disabled]) .control:hover .checked-indicator {
        fill: ${jr.GrayText};
        background: ${jr.GrayText};
      }
    `)),ci=rr.Radio.compose({baseName:"radio",template:rr.radioTemplate,styles:si,checkedIndicator:'\n    <div part="checked-indicator" class="checked-indicator"></div>\n  '}),di=(e,t)=>Br.css`
    ${(0,ae.display)("flex")} :host {
        align-items: flex-start;
        margin: calc(${me} * 1px) 0;
        flex-direction: column;
    }
    .positioning-region {
        display: flex;
        flex-wrap: wrap;
    }
    :host([orientation="vertical"]) .positioning-region {
        flex-direction: column;
    }
    :host([orientation="horizontal"]) .positioning-region {
        flex-direction: row;
    }
`,hi=rr.RadioGroup.compose({baseName:"radio-group",template:rr.radioGroupTemplate,styles:di}),ui=ae.DesignToken.create("clear-button-hover").withDefault((e=>{const t=go.getValueFor(e),o=ro.getValueFor(e);return t.evaluate(e,o.evaluate(e).hover).hover})),pi=ae.DesignToken.create("clear-button-active").withDefault((e=>{const t=go.getValueFor(e),o=ro.getValueFor(e);return t.evaluate(e,o.evaluate(e).hover).active}));class gi extends ae.Search{constructor(){super(...arguments),this.appearance="outline"}}(0,Ir.gn)([Br.attr],gi.prototype,"appearance",void 0),gi.compose({baseName:"search",baseClass:ae.Search,template:ae.searchTemplate,styles:(e,t)=>Br.css`
    ${(0,ae.display)("inline-block")} :host {
        font-family: ${pe};
        outline: none;
        user-select: none;
    }

    .root {
        box-sizing: border-box;
        position: relative;
        display: flex;
        flex-direction: row;
        color: ${Ho};
        background: ${co};
        border-radius: calc(${$e} * 1px);
        border: calc(${we} * 1px) solid ${Rt};
        height: calc(${Mr} * 1px);
        align-items: baseline;
    }

    .control {
        -webkit-appearance: none;
        font: inherit;
        background: transparent;
        border: 0;
        color: inherit;
        height: calc(100% - 4px);
        width: 100%;
        margin-top: auto;
        margin-bottom: auto;
        border: none;
        padding: 0 calc(${me} * 2px + 1px);
        font-size: ${Fe};
        line-height: ${Te};
    }

    .control::-webkit-search-cancel-button {
        -webkit-appearance: none;
    }

    .control:hover,
    .control:${ae.focusVisible},
    .control:disabled,
    .control:active {
        outline: none;
    }

    .clear-button {
        height: calc(100% - 2px);
        opacity: 0;
        margin: 1px;
        background: transparent;
        color: ${Ho};
        fill: currentcolor;
        border: none;
        border-radius: calc(${$e} * 1px);
        min-width: calc(${Mr} * 1px);
        font-size: ${Fe};
        line-height: ${Te};
        outline: none;
        font-family: ${pe};
        padding: 0 calc((10 + (${me} * 2 * ${xe})) * 1px);
    }

    .clear-button:hover {
        background: ${fo};
    }

    .clear-button:active {
        background: ${$o};
    }

    :host([appearance="filled"]) .clear-button:hover {
        background: ${ui};
    }

    :host([appearance="filled"]) .clear-button:active {
        background: ${pi};
    }

    .input-wrapper {
        display: flex;
        position: relative;
        width: 100%;
        height: 100%;
    }

    .label {
        display: block;
        color: ${Ho};
        cursor: pointer;
        font-size: ${Fe};
        line-height: ${Te};
        margin-bottom: 4px;
    }

    .label__hidden {
        display: none;
        visibility: hidden;
    }

    .input-wrapper,
    .start,
    .end {
        align-self: center;
    }

    .start,
    .end {
        display: flex;
        margin: 1px;
        fill: currentcolor;
    }

    ::slotted([slot="end"]) {
        height: 100%
    }

    .end {
        margin-inline-end: 1px;
        height: calc(100% - 2px);
    }

    ::slotted(svg) {
        /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
        width: 16px;
        height: 16px;
        margin-inline-end: 11px;
        margin-inline-start: 11px;
        margin-top: auto;
        margin-bottom: auto;
    }

    :host(:hover:not([disabled])) .root {
        background: ${ho};
        border-color: ${At};
    }

    :host(:active:not([disabled])) .root {
        background: ${ho};
        border-color: ${It};
    }

    :host(:focus-within:not([disabled])) .root {
        border-color: ${Vo};
        box-shadow: 0 0 0 1px ${Vo} inset;
    }

    .clear-button__hidden {
        opacity: 0;
    }

    :host(:hover:not([disabled], [readOnly])) .clear-button,
    :host(:active:not([disabled], [readOnly])) .clear-button,
    :host(:focus-within:not([disabled], [readOnly])) .clear-button {
        opacity: 1;
    }

    :host(:hover:not([disabled], [readOnly])) .clear-button__hidden,
    :host(:active:not([disabled], [readOnly])) .clear-button__hidden,
    :host(:focus-within:not([disabled], [readOnly])) .clear-button__hidden {
        opacity: 0;
    }

    :host([appearance="filled"]) .root {
        background: ${Lt};
    }

    :host([appearance="filled"]:hover:not([disabled])) .root {
        background: ${io};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
        cursor: ${ae.disabledCursor};
    }

    :host([disabled]) {
        opacity: ${ye};
    }

    :host([disabled]) .control {
        border-color: ${Oo};
    }
`.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
                .root,
                :host([appearance="filled"]) .root {
                    forced-color-adjust: none;
                    background: ${Ar.Field};
                    border-color: ${Ar.FieldText};
                }
                :host(:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover) .root {
                    background: ${Ar.Field};
                    border-color: ${Ar.Highlight};
                }
                .start,
                .end {
                    fill: currentcolor;
                }
                :host([disabled]) {
                    opacity: 1;
                }
                :host([disabled]) .root,
                :host([appearance="filled"]:hover[disabled]) .root {
                    border-color: ${Ar.GrayText};
                    background: ${Ar.Field};
                }
                :host(:focus-within:enabled) .root {
                    border-color: ${Ar.Highlight};
                    box-shadow: 0 0 0 1px ${Ar.Highlight} inset;
                }
                input::placeholder {
                    color: ${Ar.GrayText};
                }
            `)),shadowOptions:{delegatesFocus:!0}});const bi=rr.DesignToken.create("clear-button-hover").withDefault((e=>{const t=go.getValueFor(e),o=ro.getValueFor(e);return t.evaluate(e,o.evaluate(e).hover).hover})),fi=rr.DesignToken.create("clear-button-active").withDefault((e=>{const t=go.getValueFor(e),o=ro.getValueFor(e);return t.evaluate(e,o.evaluate(e).hover).active})),$i=(e,t)=>Hr.css`
  ${Ma}

  .control {
    padding: 0;
    padding-inline-start: calc(${me} * 2px + 1px);
    padding-inline-end: calc(
      (${me} * 2px) + (${Lr} * 1px) + 1px
    );
  }

  .control::-webkit-search-cancel-button {
    -webkit-appearance: none;
  }

  .control:hover,
    .control:${rr.focusVisible},
    .control:disabled,
    .control:active {
    outline: none;
  }

  .clear-button {
    height: calc(100% - 2px);
    opacity: 0;
    margin: 1px;
    background: transparent;
    color: ${Ho};
    fill: currentcolor;
    border: none;
    border-radius: calc(${$e} * 1px);
    min-width: calc(${Lr} * 1px);
    font-size: ${Fe};
    line-height: ${Te};
    outline: none;
    font-family: ${pe};
    padding: 0 calc((10 + (${me} * 2 * ${xe})) * 1px);
  }

  .clear-button:hover {
    background: ${fo};
  }

  .clear-button:active {
    background: ${$o};
  }

  :host([appearance='filled']) .clear-button:hover {
    background: ${bi};
  }

  :host([appearance='filled']) .clear-button:active {
    background: ${fi};
  }

  .input-wrapper {
    display: flex;
    position: relative;
    width: 100%;
  }

  .start,
  .end {
    display: flex;
    margin: 1px;
  }

  ::slotted([slot='end']) {
    height: 100%;
  }

  .end {
    margin-inline-end: 1px;
  }

  ::slotted(svg) {
    /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
    margin-inline-end: 11px;
    margin-inline-start: 11px;
    margin-top: auto;
    margin-bottom: auto;
  }

  .clear-button__hidden {
    opacity: 0;
  }

  :host(:hover:not([disabled], [readOnly])) .clear-button,
  :host(:active:not([disabled], [readOnly])) .clear-button,
  :host(:focus-within:not([disabled], [readOnly])) .clear-button {
    opacity: 1;
  }

  :host(:hover:not([disabled], [readOnly])) .clear-button__hidden,
  :host(:active:not([disabled], [readOnly])) .clear-button__hidden,
  :host(:focus-within:not([disabled], [readOnly])) .clear-button__hidden {
    opacity: 0;
  }
`,xi=gi.compose({baseName:"search",baseClass:rr.Search,template:rr.searchTemplate,styles:$i,shadowOptions:{delegatesFocus:!0}});class mi extends rr.Select{connectedCallback(){super.connectedCallback(),this.setAutoWidth()}slottedOptionsChanged(e,t){super.slottedOptionsChanged(e,t),this.setAutoWidth()}autoWidthChanged(e,t){t?this.setAutoWidth():this.style.removeProperty("width")}setAutoWidth(){if(!this.autoWidth||!this.isConnected)return;let e=this.listbox.getBoundingClientRect().width;0===e&&this.listbox.hidden&&(Object.assign(this.listbox.style,{visibility:"hidden"}),this.listbox.removeAttribute("hidden"),e=this.listbox.getBoundingClientRect().width,this.listbox.setAttribute("hidden",""),this.listbox.style.removeProperty("visibility")),e>0&&Object.assign(this.style,{width:`${e}px`})}}(0,Ir.gn)([(0,Hr.attr)({attribute:"autowidth",mode:"boolean"})],mi.prototype,"autoWidth",void 0),(0,Ir.gn)([(0,Hr.attr)({attribute:"minimal",mode:"boolean"})],mi.prototype,"minimal",void 0);const vi=mi.compose({baseName:"select",baseClass:rr.Select,template:rr.selectTemplate,styles:Ta,indicator:'\n        <svg\n            class="select-indicator"\n            part="select-indicator"\n            viewBox="0 0 12 7"\n            xmlns="http://www.w3.org/2000/svg"\n        >\n            <path\n                d="M11.85.65c.2.2.2.5 0 .7L6.4 6.84a.55.55 0 01-.78 0L.14 1.35a.5.5 0 11.71-.7L6 5.8 11.15.65c.2-.2.5-.2.7 0z"\n            />\n        </svg>\n    '}),yi=rr.Slider.compose({baseName:"slider",template:rr.sliderTemplate,styles:(e,t)=>Hr.css`
    :host([hidden]) {
      display: none;
    }

    ${(0,rr.display)("inline-grid")} :host {
      --thumb-size: calc(${Lr} * 0.5 - ${me});
      --thumb-translate: calc(
        var(--thumb-size) * -0.5 + var(--track-width) / 2
      );
      --track-overhang: calc((${me} / 2) * -1);
      --track-width: ${me};
      --jp-slider-height: calc(var(--thumb-size) * 10);
      align-items: center;
      width: 100%;
      margin: calc(${me} * 1px) 0;
      user-select: none;
      box-sizing: border-box;
      border-radius: calc(${$e} * 1px);
      outline: none;
      cursor: pointer;
    }
    :host([orientation='horizontal']) .positioning-region {
      position: relative;
      margin: 0 8px;
      display: grid;
      grid-template-rows: calc(var(--thumb-size) * 1px) 1fr;
    }
    :host([orientation='vertical']) .positioning-region {
      position: relative;
      margin: 0 8px;
      display: grid;
      height: 100%;
      grid-template-columns: calc(var(--thumb-size) * 1px) 1fr;
    }

    :host(:${rr.focusVisible}) .thumb-cursor {
      box-shadow:
        0 0 0 2px ${Lt},
        0 0 0 calc((2 + ${ke}) * 1px) ${Mt};
    }

    .thumb-container {
      position: absolute;
      height: calc(var(--thumb-size) * 1px);
      width: calc(var(--thumb-size) * 1px);
      transition: all 0.2s ease;
      color: ${Ho};
      fill: currentcolor;
    }
    .thumb-cursor {
      border: none;
      width: calc(var(--thumb-size) * 1px);
      height: calc(var(--thumb-size) * 1px);
      background: ${Ho};
      border-radius: calc(${$e} * 1px);
    }
    .thumb-cursor:hover {
      background: ${Ho};
      border-color: ${No};
    }
    .thumb-cursor:active {
      background: ${Ho};
    }
    :host([orientation='horizontal']) .thumb-container {
      transform: translateX(calc(var(--thumb-size) * 0.5px))
        translateY(calc(var(--thumb-translate) * 1px));
    }
    :host([orientation='vertical']) .thumb-container {
      transform: translateX(calc(var(--thumb-translate) * 1px))
        translateY(calc(var(--thumb-size) * 0.5px));
    }
    :host([orientation='horizontal']) {
      min-width: calc(var(--thumb-size) * 1px);
    }
    :host([orientation='horizontal']) .track {
      right: calc(var(--track-overhang) * 1px);
      left: calc(var(--track-overhang) * 1px);
      align-self: start;
      height: calc(var(--track-width) * 1px);
    }
    :host([orientation='vertical']) .track {
      top: calc(var(--track-overhang) * 1px);
      bottom: calc(var(--track-overhang) * 1px);
      width: calc(var(--track-width) * 1px);
      height: 100%;
    }
    .track {
      background: ${Oo};
      position: absolute;
      border-radius: calc(${$e} * 1px);
    }
    :host([orientation='vertical']) {
      height: calc(var(--jp-slider-height) * 1px);
      min-height: calc(var(--thumb-size) * 1px);
      min-width: calc(${me} * 20px);
    }
    :host([disabled]),
    :host([readonly]) {
      cursor: ${rr.disabledCursor};
    }
    :host([disabled]) {
      opacity: ${ye};
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      .thumb-cursor {
        forced-color-adjust: none;
        border-color: ${jr.FieldText};
        background: ${jr.FieldText};
      }
      .thumb-cursor:hover,
      .thumb-cursor:active {
        background: ${jr.Highlight};
      }
      .track {
        forced-color-adjust: none;
        background: ${jr.FieldText};
      }
      :host(:${rr.focusVisible}) .thumb-cursor {
        border-color: ${jr.Highlight};
      }
      :host([disabled]) {
        opacity: 1;
      }
      :host([disabled]) .track,
      :host([disabled]) .thumb-cursor {
        forced-color-adjust: none;
        background: ${jr.GrayText};
      }

      :host(:${rr.focusVisible}) .thumb-cursor {
        background: ${jr.Highlight};
        border-color: ${jr.Highlight};
        box-shadow:
          0 0 0 2px ${jr.Field},
          0 0 0 4px ${jr.FieldText};
      }
    `)),thumb:'\n        <div class="thumb-cursor"></div>\n    '});var wi=o(899);const ki=Br.css`
    :host {
        align-self: start;
        grid-row: 2;
        margin-top: -2px;
        height: calc((${Mr} / 2 + ${me}) * 1px);
        width: auto;
    }
    .container {
        grid-template-rows: auto auto;
        grid-template-columns: 0;
    }
    .label {
        margin: 2px 0;
    }
`,Fi=Br.css`
    :host {
        justify-self: start;
        grid-column: 2;
        margin-left: 2px;
        height: auto;
        width: calc((${Mr} / 2 + ${me}) * 1px);
    }
    .container {
        grid-template-columns: auto auto;
        grid-template-rows: 0;
        min-width: calc(var(--thumb-size) * 1px);
        height: calc(var(--thumb-size) * 1px);
    }
    .mark {
        transform: rotate(90deg);
        align-self: center;
    }
    .label {
        margin-left: calc((${me} / 2) * 3px);
        align-self: center;
    }
`,Ti=(e,t)=>Br.css`
        ${(0,ae.display)("block")} :host {
            font-family: ${pe};
            color: ${Ho};
            fill: currentcolor;
        }
        .root {
            position: absolute;
            display: grid;
        }
        .container {
            display: grid;
            justify-self: center;
        }
        .label {
            justify-self: center;
            align-self: center;
            white-space: nowrap;
            max-width: 30px;
        }
        .mark {
            width: calc((${me} / 4) * 1px);
            height: calc(${Mr} * 0.25 * 1px);
            background: ${Oo};
            justify-self: center;
        }
        :host(.disabled) {
            opacity: ${ye};
        }
    `.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
                .mark {
                    forced-color-adjust: none;
                    background: ${Ar.FieldText};
                }
                :host(.disabled) {
                    forced-color-adjust: none;
                    opacity: 1;
                }
                :host(.disabled) .label {
                    color: ${Ar.GrayText};
                }
                :host(.disabled) .mark {
                    background: ${Ar.GrayText};
                }
            `));class Ci extends ae.SliderLabel{sliderOrientationChanged(){this.sliderOrientation===wi.i.horizontal?(this.$fastController.addStyles(ki),this.$fastController.removeStyles(Fi)):(this.$fastController.addStyles(Fi),this.$fastController.removeStyles(ki))}}Ci.compose({baseName:"slider-label",baseClass:ae.SliderLabel,template:ae.sliderLabelTemplate,styles:Ti});const Vi=Ci.compose({baseName:"slider-label",baseClass:rr.SliderLabel,template:rr.sliderLabelTemplate,styles:Ti}),Di=rr.Switch.compose({baseName:"switch",template:rr.switchTemplate,styles:(e,t)=>Hr.css`
    :host([hidden]) {
      display: none;
    }

    ${(0,rr.display)("inline-flex")} :host {
      align-items: center;
      outline: none;
      font-family: ${pe};
      margin: calc(${me} * 1px) 0;
      ${""} user-select: none;
    }

    :host([disabled]) {
      opacity: ${ye};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .switch,
    :host([disabled]) .switch {
      cursor: ${rr.disabledCursor};
    }

    .switch {
      position: relative;
      outline: none;
      box-sizing: border-box;
      width: calc(${Lr} * 1px);
      height: calc((${Lr} / 2 + ${me}) * 1px);
      background: ${co};
      border-radius: calc(${$e} * 1px);
      border: calc(${we} * 1px) solid ${Oo};
    }

    .switch:hover {
      background: ${ho};
      border-color: ${No};
      cursor: pointer;
    }

    host([disabled]) .switch:hover,
    host([readonly]) .switch:hover {
      background: ${ho};
      border-color: ${No};
      cursor: ${rr.disabledCursor};
    }

    :host(:not([disabled])) .switch:active {
      background: ${uo};
      border-color: ${Ro};
    }

    :host(:${rr.focusVisible}) .switch {
      outline-offset: 2px;
      outline: solid calc(${ke} * 1px) ${Mt};
    }

    .checked-indicator {
      position: absolute;
      top: 5px;
      bottom: 5px;
      background: ${Ho};
      border-radius: calc(${$e} * 1px);
      transition: all 0.2s ease-in-out;
    }

    .status-message {
      color: ${Ho};
      cursor: pointer;
      font-size: ${Fe};
      line-height: ${Te};
    }

    :host([disabled]) .status-message,
    :host([readonly]) .status-message {
      cursor: ${rr.disabledCursor};
    }

    .label {
      color: ${Ho};

      ${""} margin-inline-end: calc(${me} * 2px + 2px);
      font-size: ${Fe};
      line-height: ${Te};
      cursor: pointer;
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    ::slotted([slot='checked-message']),
    ::slotted([slot='unchecked-message']) {
      margin-inline-start: calc(${me} * 2px + 2px);
    }

    :host([aria-checked='true']) .checked-indicator {
      background: ${_t};
    }

    :host([aria-checked='true']) .switch {
      background: ${Rt};
      border-color: ${Rt};
    }

    :host([aria-checked='true']:not([disabled])) .switch:hover {
      background: ${At};
      border-color: ${At};
    }

    :host([aria-checked='true']:not([disabled]))
      .switch:hover
      .checked-indicator {
      background: ${Et};
    }

    :host([aria-checked='true']:not([disabled])) .switch:active {
      background: ${It};
      border-color: ${It};
    }

    :host([aria-checked='true']:not([disabled]))
      .switch:active
      .checked-indicator {
      background: ${qt};
    }

    :host([aria-checked="true"]:${rr.focusVisible}:not([disabled])) .switch {
      outline: solid calc(${ke} * 1px) ${Mt};
    }

    .unchecked-message {
      display: block;
    }

    .checked-message {
      display: none;
    }

    :host([aria-checked='true']) .unchecked-message {
      display: none;
    }

    :host([aria-checked='true']) .checked-message {
      display: block;
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      .checked-indicator,
      :host(:not([disabled])) .switch:active .checked-indicator {
        forced-color-adjust: none;
        background: ${jr.FieldText};
      }
      .switch {
        forced-color-adjust: none;
        background: ${jr.Field};
        border-color: ${jr.FieldText};
      }
      :host(:not([disabled])) .switch:hover {
        background: ${jr.HighlightText};
        border-color: ${jr.Highlight};
      }
      :host([aria-checked='true']) .switch {
        background: ${jr.Highlight};
        border-color: ${jr.Highlight};
      }
      :host([aria-checked='true']:not([disabled])) .switch:hover,
      :host(:not([disabled])) .switch:active {
        background: ${jr.HighlightText};
        border-color: ${jr.Highlight};
      }
      :host([aria-checked='true']) .checked-indicator {
        background: ${jr.HighlightText};
      }
      :host([aria-checked='true']:not([disabled]))
        .switch:hover
        .checked-indicator {
        background: ${jr.Highlight};
      }
      :host([disabled]) {
        opacity: 1;
      }
      :host(:${rr.focusVisible}) .switch {
        border-color: ${jr.Highlight};
        outline-offset: 2px;
        outline: solid calc(${ke} * 1px) ${jr.FieldText};
      }
      :host([aria-checked="true"]:${rr.focusVisible}:not([disabled])) .switch {
        outline: solid calc(${ke} * 1px) ${jr.FieldText};
      }
      :host([disabled]) .checked-indicator {
        background: ${jr.GrayText};
      }
      :host([disabled]) .switch {
        background: ${jr.Field};
        border-color: ${jr.GrayText};
      }
    `),new ar(Hr.css`
        .checked-indicator {
          left: 5px;
          right: calc(((${Lr} / 2) + 1) * 1px);
        }

        :host([aria-checked='true']) .checked-indicator {
          left: calc(((${Lr} / 2) + 1) * 1px);
          right: 5px;
        }
      `,Hr.css`
        .checked-indicator {
          right: 5px;
          left: calc(((${Lr} / 2) + 1) * 1px);
        }

        :host([aria-checked='true']) .checked-indicator {
          right: calc(((${Lr} / 2) + 1) * 1px);
          left: 5px;
        }
      `)),switch:'\n    <span class="checked-indicator" part="checked-indicator"></span>\n  '}),Si=(e,t)=>Br.css`
    ${(0,ae.display)("block")} :host {
        box-sizing: border-box;
        font-size: ${Fe};
        line-height: ${Te};
        padding: 0 calc((6 + (${me} * 2 * ${xe})) * 1px);
    }
`,Bi=rr.TabPanel.compose({baseName:"tab-panel",template:rr.tabPanelTemplate,styles:Si}),zi=(e,t)=>Hr.css`
    ${(0,rr.display)("inline-flex")} :host {
      box-sizing: border-box;
      font-family: ${pe};
      font-size: ${Fe};
      line-height: ${Te};
      height: calc(${Lr} * 1px);
      padding: calc(${me} * 5px) calc(${me} * 4px);
      color: ${zo};
      fill: currentcolor;
      border-radius: 0 0 calc(${$e} * 1px)
        calc(${$e} * 1px);
      border: calc(${we} * 1px) solid transparent;
      align-items: center;
      grid-row: 2;
      justify-content: center;
      cursor: pointer;
    }

    :host(:hover) {
      color: ${Ho};
      fill: currentcolor;
    }

    :host(:active) {
      color: ${Ho};
      fill: currentcolor;
    }

    :host([disabled]) {
      cursor: ${rr.disabledCursor};
      opacity: ${ye};
    }

    :host([disabled]:hover) {
      color: ${zo};
      background: ${bo};
    }

    :host([aria-selected='true']) {
      background: ${ao};
      color: ${Ho};
      fill: currentcolor;
    }

    :host([aria-selected='true']:hover) {
      background: ${io};
      color: ${Ho};
      fill: currentcolor;
    }

    :host([aria-selected='true']:active) {
      background: ${lo};
      color: ${Ho};
      fill: currentcolor;
    }

    :host(:${rr.focusVisible}) {
      outline: none;
      border-color: ${Mt};
      box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px)
        ${Mt};
    }

    :host(:focus) {
      outline: none;
    }

    :host(.vertical) {
      justify-content: end;
      grid-column: 2;
      border-bottom-left-radius: 0;
      border-top-right-radius: calc(${$e} * 1px);
    }

    :host(.vertical[aria-selected='true']) {
      z-index: 2;
    }

    :host(.vertical:hover) {
      color: ${Ho};
    }

    :host(.vertical:active) {
      color: ${Ho};
    }

    :host(.vertical:hover[aria-selected='true']) {
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      :host {
        forced-color-adjust: none;
        border-color: transparent;
        color: ${jr.ButtonText};
        fill: currentcolor;
      }
      :host(:hover),
      :host(.vertical:hover),
      :host([aria-selected='true']:hover) {
        background: ${jr.Highlight};
        color: ${jr.HighlightText};
        fill: currentcolor;
      }
      :host([aria-selected='true']) {
        background: ${jr.HighlightText};
        color: ${jr.Highlight};
        fill: currentcolor;
      }
      :host(:${rr.focusVisible}) {
        border-color: ${jr.ButtonText};
        box-shadow: none;
      }
      :host([disabled]),
      :host([disabled]:hover) {
        opacity: 1;
        color: ${jr.GrayText};
        background: ${jr.ButtonFace};
      }
    `)),ji=rr.Tab.compose({baseName:"tab",template:rr.tabTemplate,styles:zi}),Hi=(e,t)=>Hr.css`
    ${(0,rr.display)("grid")} :host {
      box-sizing: border-box;
      font-family: ${pe};
      font-size: ${Fe};
      line-height: ${Te};
      color: ${Ho};
      grid-template-columns: auto 1fr auto;
      grid-template-rows: auto 1fr;
    }

    .tablist {
      display: grid;
      grid-template-rows: auto auto;
      grid-template-columns: auto;
      position: relative;
      width: max-content;
      align-self: end;
      padding: calc(${me} * 4px) calc(${me} * 4px) 0;
      box-sizing: border-box;
    }

    .start,
    .end {
      align-self: center;
    }

    .activeIndicator {
      grid-row: 1;
      grid-column: 1;
      width: 100%;
      height: 4px;
      justify-self: center;
      background: ${Rt};
      margin-top: 0;
      border-radius: calc(${$e} * 1px)
        calc(${$e} * 1px) 0 0;
    }

    .activeIndicatorTransition {
      transition: transform 0.01s ease-in-out;
    }

    .tabpanel {
      grid-row: 2;
      grid-column-start: 1;
      grid-column-end: 4;
      position: relative;
    }

    :host([orientation='vertical']) {
      grid-template-rows: auto 1fr auto;
      grid-template-columns: auto 1fr;
    }

    :host([orientation='vertical']) .tablist {
      grid-row-start: 2;
      grid-row-end: 2;
      display: grid;
      grid-template-rows: auto;
      grid-template-columns: auto 1fr;
      position: relative;
      width: max-content;
      justify-self: end;
      align-self: flex-start;
      width: 100%;
      padding: 0 calc(${me} * 4px)
        calc((${Lr} - ${me}) * 1px) 0;
    }

    :host([orientation='vertical']) .tabpanel {
      grid-column: 2;
      grid-row-start: 1;
      grid-row-end: 4;
    }

    :host([orientation='vertical']) .end {
      grid-row: 3;
    }

    :host([orientation='vertical']) .activeIndicator {
      grid-column: 1;
      grid-row: 1;
      width: 4px;
      height: 100%;
      margin-inline-end: 0px;
      align-self: center;
      border-radius: calc(${$e} * 1px) 0 0
        calc(${$e} * 1px);
    }

    :host([orientation='vertical']) .activeIndicatorTransition {
      transition: transform 0.01s ease-in-out;
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      .activeIndicator,
      :host([orientation='vertical']) .activeIndicator {
        forced-color-adjust: none;
        background: ${jr.Highlight};
      }
    `)),Li=rr.Tabs.compose({baseName:"tabs",template:rr.tabsTemplate,styles:Hi});class Oi extends ae.TextArea{constructor(){super(...arguments),this.appearance="outline"}}(0,Ir.gn)([Br.attr],Oi.prototype,"appearance",void 0),Oi.compose({baseName:"text-area",baseClass:ae.TextArea,template:ae.textAreaTemplate,styles:(e,t)=>Br.css`
    ${(0,ae.display)("inline-block")} :host {
        font-family: ${pe};
        outline: none;
        user-select: none;
    }

    .control {
        box-sizing: border-box;
        position: relative;
        color: ${Ho};
        background: ${co};
        border-radius: calc(${$e} * 1px);
        border: calc(${we} * 1px) solid ${Rt};
        height: calc(${Mr} * 2px);
        font: inherit;
        font-size: ${Fe};
        line-height: ${Te};
        padding: calc(${me} * 2px + 1px);
        width: 100%;
        resize: none;
    }

    .control:hover:enabled {
        background: ${ho};
        border-color: ${At};
    }

    .control:active:enabled {
        background: ${uo};
        border-color: ${It};
    }

    .control:hover,
    .control:${ae.focusVisible},
    .control:disabled,
    .control:active {
        outline: none;
    }

    :host(:focus-within) .control {
        border-color: ${Vo};
        box-shadow: 0 0 0 1px ${Vo} inset;
    }

    :host([appearance="filled"]) .control {
        background: ${ao};
    }

    :host([appearance="filled"]:hover:not([disabled])) .control {
        background: ${io};
    }

    :host([resize="both"]) .control {
        resize: both;
    }

    :host([resize="horizontal"]) .control {
        resize: horizontal;
    }

    :host([resize="vertical"]) .control {
        resize: vertical;
    }

    .label {
        display: block;
        color: ${Ho};
        cursor: pointer;
        font-size: ${Fe};
        line-height: ${Te};
        margin-bottom: 4px;
    }

    .label__hidden {
        display: none;
        visibility: hidden;
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
        cursor: ${ae.disabledCursor};
    }
    :host([disabled]) {
        opacity: ${ye};
    }
    :host([disabled]) .control {
        border-color: ${Oo};
    }

    :host([cols]){
        width: initial;
    }

    :host([rows]) .control {
        height: initial;
    }
 `.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
                :host([disabled]) {
                    opacity: 1;
                }
            `)),shadowOptions:{delegatesFocus:!0}});const Ni=(e,t)=>Hr.css`
    ${(0,rr.display)("inline-block")} :host {
      font-family: ${pe};
      outline: none;
      user-select: none;
    }

    .control {
      box-sizing: border-box;
      position: relative;
      color: ${Ho};
      background: ${co};
      border-radius: calc(${$e} * 1px);
      border: calc(${we} * 1px) solid ${vo};
      height: calc(${Lr} * 2px);
      font: inherit;
      font-size: ${Fe};
      line-height: ${Te};
      padding: calc(${me} * 2px + 1px);
      width: 100%;
      resize: none;
    }

    .control:hover:enabled {
      background: ${ho};
      border-color: ${yo};
    }

    .control:active:enabled {
      background: ${uo};
      border-color: ${wo};
    }

    .control:hover,
    .control:${rr.focusVisible},
    .control:disabled,
    .control:active {
      outline: none;
    }

    :host(:focus-within) .control {
      border-color: ${Mt};
      box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px)
        ${Mt};
    }

    :host([appearance='filled']) .control {
      background: ${ao};
    }

    :host([appearance='filled']:hover:not([disabled])) .control {
      background: ${io};
    }

    :host([resize='both']) .control {
      resize: both;
    }

    :host([resize='horizontal']) .control {
      resize: horizontal;
    }

    :host([resize='vertical']) .control {
      resize: vertical;
    }

    .label {
      display: block;
      color: ${Ho};
      cursor: pointer;
      font-size: ${Fe};
      line-height: ${Te};
      margin-bottom: 4px;
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
      cursor: ${rr.disabledCursor};
    }
    :host([disabled]) {
      opacity: ${ye};
    }
    :host([disabled]) .control {
      border-color: ${Oo};
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      :host([disabled]) {
        opacity: 1;
      }
    `)),Ri=Oi.compose({baseName:"text-area",baseClass:rr.TextArea,template:rr.textAreaTemplate,styles:Ni,shadowOptions:{delegatesFocus:!0}});class Ai extends ae.TextField{constructor(){super(...arguments),this.appearance="outline"}}(0,Ir.gn)([Br.attr],Ai.prototype,"appearance",void 0),Ai.compose({baseName:"text-field",baseClass:ae.TextField,template:ae.textFieldTemplate,styles:(e,t)=>Br.css`
    ${(0,ae.display)("inline-block")} :host {
        font-family: ${pe};
        outline: none;
        user-select: none;
    }

    .root {
        box-sizing: border-box;
        position: relative;
        display: flex;
        flex-direction: row;
        color: ${Ho};
        background: ${co};
        border-radius: calc(${$e} * 1px);
        border: calc(${we} * 1px) solid ${Rt};
        height: calc(${Mr} * 1px);
        align-items: baseline;
    }

    .control {
        -webkit-appearance: none;
        font: inherit;
        background: transparent;
        border: 0;
        color: inherit;
        height: calc(100% - 4px);
        width: 100%;
        margin-top: auto;
        margin-bottom: auto;
        border: none;
        padding: 0 calc(${me} * 2px + 1px);
        font-size: ${Fe};
        line-height: ${Te};
    }

    .control:hover,
    .control:${ae.focusVisible},
    .control:disabled,
    .control:active {
        outline: none;
    }

    .label {
        display: block;
        color: ${Ho};
        cursor: pointer;
        font-size: ${Fe};
        line-height: ${Te};
        margin-bottom: 4px;
    }

    .label__hidden {
        display: none;
        visibility: hidden;
    }

    .start,
    .control,
    .end {
        align-self: center;
    }

    .start,
    .end {
        display: flex;
        margin: auto;
        fill: currentcolor;
    }

    ::slotted(svg) {
        /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
        width: 16px;
        height: 16px;
    }

    .start {
        margin-inline-start: 11px;
    }

    .end {
        margin-inline-end: 11px;
    }

    :host(:hover:not([disabled])) .root {
        background: ${ho};
        border-color: ${At};
    }

    :host(:active:not([disabled])) .root {
        background: ${ho};
        border-color: ${It};
    }

    :host(:focus-within:not([disabled])) .root {
        border-color: ${Vo};
        box-shadow: 0 0 0 calc(${ke} * 1px) ${Vo} inset;
    }

    :host([appearance="filled"]) .root {
        background: ${ao};
    }

    :host([appearance="filled"]:hover:not([disabled])) .root {
        background: ${io};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
        cursor: ${ae.disabledCursor};
    }

    :host([disabled]) {
        opacity: ${ye};
    }

    :host([disabled]) .control {
        border-color: ${Oo};
    }
`.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
                .root,
                :host([appearance="filled"]) .root {
                    forced-color-adjust: none;
                    background: ${Ar.Field};
                    border-color: ${Ar.FieldText};
                }
                :host(:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover) .root {
                    background: ${Ar.Field};
                    border-color: ${Ar.Highlight};
                }
                .start,
                .end {
                    fill: currentcolor;
                }
                :host([disabled]) {
                    opacity: 1;
                }
                :host([disabled]) .root,
                :host([appearance="filled"]:hover[disabled]) .root {
                    border-color: ${Ar.GrayText};
                    background: ${Ar.Field};
                }
                :host(:focus-within:enabled) .root {
                    border-color: ${Ar.Highlight};
                    box-shadow: 0 0 0 1px ${Ar.Highlight} inset;
                }
                input::placeholder {
                    color: ${Ar.GrayText};
                }
            `)),shadowOptions:{delegatesFocus:!0}});const Ii=(e,t)=>Hr.css`
  ${Ma}

  .start,
    .end {
    display: flex;
  }
`,Mi=Ai.compose({baseName:"text-field",baseClass:rr.TextField,template:rr.textFieldTemplate,styles:Ii,shadowOptions:{delegatesFocus:!0}});class Pi extends ae.Toolbar{connectedCallback(){super.connectedCallback();const e=(0,ae.composedParent)(this);e&&Lt.setValueFor(this,(t=>Fo.getValueFor(t).evaluate(t,Lt.getValueFor(e))))}}Pi.compose({baseName:"toolbar",baseClass:ae.Toolbar,template:ae.toolbarTemplate,styles:(e,t)=>Br.css`
        ${(0,ae.display)("inline-flex")} :host {
            --toolbar-item-gap: calc(
                (var(--design-unit) + calc(var(--density) + 2)) * 1px
            );
            background-color: ${Lt};
            border-radius: calc(${$e} * 1px);
            fill: currentcolor;
            padding: var(--toolbar-item-gap);
        }

        :host(${ae.focusVisible}) {
            outline: calc(${we} * 1px) solid ${Ao};
        }

        .positioning-region {
            align-items: flex-start;
            display: inline-flex;
            flex-flow: row wrap;
            justify-content: flex-start;
        }

        :host([orientation="vertical"]) .positioning-region {
            flex-direction: column;
        }

        ::slotted(:not([slot])) {
            flex: 0 0 auto;
            margin: 0 var(--toolbar-item-gap);
        }

        :host([orientation="vertical"]) ::slotted(:not([slot])) {
            margin: var(--toolbar-item-gap) 0;
        }

        .start,
        .end {
            display: flex;
            margin: auto;
            margin-inline: 0;
        }

        ::slotted(svg) {
            /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
            width: 16px;
            height: 16px;
        }
    `.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
            :host(:${ae.focusVisible}) {
                box-shadow: 0 0 0 calc(${ke} * 1px) ${Ar.Highlight};
                color: ${Ar.ButtonText};
                forced-color-adjust: none;
            }
        `)),shadowOptions:{delegatesFocus:!0}});const Gi=(e,t)=>Hr.css`
    ${(0,rr.display)("inline-flex")} :host {
      --toolbar-item-gap: calc(
        (var(--design-unit) + calc(var(--density) + 2)) * 1px
      );
      background-color: ${Lt};
      border-radius: calc(${$e} * 1px);
      fill: currentcolor;
      padding: var(--toolbar-item-gap);
    }

    :host(${rr.focusVisible}) {
      outline: calc(${we} * 1px) solid ${Mt};
    }

    .positioning-region {
      align-items: flex-start;
      display: inline-flex;
      flex-flow: row wrap;
      justify-content: flex-start;
      width: 100%;
      height: 100%;
    }

    :host([orientation='vertical']) .positioning-region {
      flex-direction: column;
    }

    ::slotted(:not([slot])) {
      flex: 0 0 auto;
      margin: 0 var(--toolbar-item-gap);
    }

    :host([orientation='vertical']) ::slotted(:not([slot])) {
      margin: var(--toolbar-item-gap) 0;
    }

    .start,
    .end {
      display: flex;
      margin: auto;
      margin-inline: 0;
    }

    ::slotted(svg) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;
    }
  `.withBehaviors((0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      :host(:${rr.focusVisible}) {
        box-shadow: 0 0 0 calc(${ke} * 1px)
          ${jr.Highlight};
        color: ${jr.ButtonText};
        forced-color-adjust: none;
      }
    `)),_i=Pi.compose({baseName:"toolbar",baseClass:rr.Toolbar,template:rr.toolbarTemplate,styles:Gi,shadowOptions:{delegatesFocus:!0}}),Ei=(e,t)=>{const o=e.tagFor(ae.AnchoredRegion);return Br.css`
            :host {
                contain: size;
                overflow: visible;
                height: 0;
                width: 0;
            }

            .tooltip {
                box-sizing: border-box;
                border-radius: calc(${$e} * 1px);
                border: calc(${we} * 1px) solid ${Vo};
                box-shadow: 0 0 0 1px ${Vo} inset;
                background: ${ao};
                color: ${Ho};
                padding: 4px;
                height: fit-content;
                width: fit-content;
                font-family: ${pe};
                font-size: ${Fe};
                line-height: ${Te};
                white-space: nowrap;
                /* TODO: a mechanism to manage z-index across components
                    https://github.com/microsoft/fast/issues/3813 */
                z-index: 10000;
            }

            ${o} {
                display: flex;
                justify-content: center;
                align-items: center;
                overflow: visible;
                flex-direction: row;
            }

            ${o}.right,
            ${o}.left {
                flex-direction: column;
            }

            ${o}.top .tooltip {
                margin-bottom: 4px;
            }

            ${o}.bottom .tooltip {
                margin-top: 4px;
            }

            ${o}.left .tooltip {
                margin-right: 4px;
            }

            ${o}.right .tooltip {
                margin-left: 4px;
            }

            ${o}.top.left .tooltip,
            ${o}.top.right .tooltip {
                margin-bottom: 0px;
            }

            ${o}.bottom.left .tooltip,
            ${o}.bottom.right .tooltip {
                margin-top: 0px;
            }

            ${o}.top.left .tooltip,
            ${o}.bottom.left .tooltip {
                margin-right: 0px;
            }

            ${o}.top.right .tooltip,
            ${o}.bottom.right .tooltip {
                margin-left: 0px;
            }

        `.withBehaviors((0,ae.forcedColorsStylesheetBehavior)(Br.css`
                :host([disabled]) {
                    opacity: 1;
                }
            `))},qi=rr.Tooltip.compose({baseName:"tooltip",template:rr.tooltipTemplate,styles:Ei}),Wi=Hr.css`
  .expand-collapse-glyph {
    transform: rotate(0deg);
  }
  :host(.nested) .expand-collapse-button {
    left: var(
      --expand-collapse-button-nested-width,
      calc(${Lr} * -1px)
    );
  }
  :host([selected])::after {
    left: calc(${ke} * 1px);
  }
  :host([expanded]) > .positioning-region .expand-collapse-glyph {
    transform: rotate(90deg);
  }
`,Ui=Hr.css`
  .expand-collapse-glyph {
    transform: rotate(180deg);
  }
  :host(.nested) .expand-collapse-button {
    right: var(
      --expand-collapse-button-nested-width,
      calc(${Lr} * -1px)
    );
  }
  :host([selected])::after {
    right: calc(${ke} * 1px);
  }
  :host([expanded]) > .positioning-region .expand-collapse-glyph {
    transform: rotate(90deg);
  }
`,Xi=Hr.cssPartial`((${ge} / 2) * ${me}) + ((${me} * ${xe}) / 2)`,Zi=rr.DesignToken.create("tree-item-expand-collapse-hover").withDefault((e=>{const t=go.getValueFor(e);return t.evaluate(e,t.evaluate(e).hover).hover})),Yi=rr.DesignToken.create("tree-item-expand-collapse-selected-hover").withDefault((e=>{const t=ro.getValueFor(e);return go.getValueFor(e).evaluate(e,t.evaluate(e).rest).hover})),Ji=rr.TreeItem.compose({baseName:"tree-item",template:rr.treeItemTemplate,styles:(e,t)=>Hr.css`
    ${(0,rr.display)("block")} :host {
      contain: content;
      position: relative;
      outline: none;
      color: ${Ho};
      background: ${bo};
      cursor: pointer;
      font-family: ${pe};
      --expand-collapse-button-size: calc(${Lr} * 1px);
      --tree-item-nested-width: 0;
    }

    :host(:focus) > .positioning-region {
      outline: none;
    }

    :host(:focus) .content-region {
      outline: none;
    }

    :host(:${rr.focusVisible}) .positioning-region {
      border-color: ${Mt};
      box-shadow: 0 0 0 calc((${ke} - ${we}) * 1px)
        ${Mt} inset;
      color: ${Ho};
    }

    .positioning-region {
      display: flex;
      position: relative;
      box-sizing: border-box;
      border: transparent calc(${we} * 1px) solid;
      border-radius: calc(${$e} * 1px);
      height: calc((${Lr} + 1) * 1px);
    }

    .positioning-region::before {
      content: '';
      display: block;
      width: var(--tree-item-nested-width);
      flex-shrink: 0;
    }

    .positioning-region:hover {
      background: ${fo};
    }

    .positioning-region:active {
      background: ${$o};
    }

    .content-region {
      display: inline-flex;
      align-items: center;
      white-space: nowrap;
      width: 100%;
      min-width: 0;
      height: calc(${Lr} * 1px);
      margin-inline-start: calc(${me} * 2px + 8px);
      font-size: ${Fe};
      line-height: ${Te};
      font-weight: 400;
    }

    .items {
      display: none;
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      font-size: calc(1em + (${me} + 16) * 1px);
    }

    .expand-collapse-button {
      background: none;
      border: none;
      outline: none;
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: calc((${Xi} + (${me} * 2)) * 1px);
      height: calc((${Xi} + (${me} * 2)) * 1px);
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      margin-left: 6px;
      margin-right: 6px;
    }

    .expand-collapse-glyph {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;
      transition: transform 0.1s linear;

      pointer-events: none;
      fill: currentcolor;
    }

    .start,
    .end {
      display: flex;
      fill: currentcolor;
    }

    ::slotted(svg) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;
    }

    .start {
      /* TODO: horizontalSpacing https://github.com/microsoft/fast/issues/2766 */
      margin-inline-end: calc(${me} * 2px + 2px);
    }

    .end {
      /* TODO: horizontalSpacing https://github.com/microsoft/fast/issues/2766 */
      margin-inline-start: calc(${me} * 2px + 2px);
    }

    :host([expanded]) > .items {
      display: block;
    }

    :host([disabled]) .content-region {
      opacity: ${ye};
      cursor: ${rr.disabledCursor};
    }

    :host(.nested) .content-region {
      position: relative;
      margin-inline-start: var(--expand-collapse-button-size);
    }

    :host(.nested) .expand-collapse-button {
      position: absolute;
    }

    :host(.nested) .expand-collapse-button:hover {
      background: ${Zi};
    }

    :host([selected]) .positioning-region {
      background: ${ao};
    }

    :host([selected]) .expand-collapse-button:hover {
      background: ${Yi};
    }

    :host([selected])::after {
      /* The background needs to be calculated based on the selected background state
            for this control. We currently have no way of changing that, so setting to
            accent-foreground-rest for the time being */
      background: ${Qt};
      border-radius: calc(${$e} * 1px);
      content: '';
      display: block;
      position: absolute;
      top: calc((${Lr} / 4) * 1px);
      width: 3px;
      height: calc((${Lr} / 2) * 1px);
    }

    ::slotted(${e.tagFor(rr.TreeItem)}) {
      --tree-item-nested-width: 1em;
      --expand-collapse-button-nested-width: calc(${Lr} * -1px);
    }
  `.withBehaviors(new ar(Wi,Ui),(0,rr.forcedColorsStylesheetBehavior)(Hr.css`
      :host {
        forced-color-adjust: none;
        border-color: transparent;
        background: ${jr.Field};
        color: ${jr.FieldText};
      }
      :host .content-region .expand-collapse-glyph {
        fill: ${jr.FieldText};
      }
      :host .positioning-region:hover,
      :host([selected]) .positioning-region {
        background: ${jr.Highlight};
      }
      :host .positioning-region:hover .content-region,
      :host([selected]) .positioning-region .content-region {
        color: ${jr.HighlightText};
      }
      :host .positioning-region:hover .content-region .expand-collapse-glyph,
      :host .positioning-region:hover .content-region .start,
      :host .positioning-region:hover .content-region .end,
      :host([selected]) .content-region .expand-collapse-glyph,
      :host([selected]) .content-region .start,
      :host([selected]) .content-region .end {
        fill: ${jr.HighlightText};
      }
      :host([selected])::after {
        background: ${jr.Field};
      }
      :host(:${rr.focusVisible}) .positioning-region {
        border-color: ${jr.FieldText};
        box-shadow: 0 0 0 2px inset ${jr.Field};
        color: ${jr.FieldText};
      }
      :host([disabled]) .content-region,
      :host([disabled]) .positioning-region:hover .content-region {
        opacity: 1;
        color: ${jr.GrayText};
      }
      :host([disabled]) .content-region .expand-collapse-glyph,
      :host([disabled]) .content-region .start,
      :host([disabled]) .content-region .end,
      :host([disabled])
        .positioning-region:hover
        .content-region
        .expand-collapse-glyph,
      :host([disabled]) .positioning-region:hover .content-region .start,
      :host([disabled]) .positioning-region:hover .content-region .end {
        fill: ${jr.GrayText};
      }
      :host([disabled]) .positioning-region:hover {
        background: ${jr.Field};
      }
      .expand-collapse-glyph,
      .start,
      .end {
        fill: ${jr.FieldText};
      }
      :host(.nested) .expand-collapse-button:hover {
        background: ${jr.Field};
      }
      :host(.nested) .expand-collapse-button:hover .expand-collapse-glyph {
        fill: ${jr.FieldText};
      }
    `)),expandCollapseGlyph:'\n        <svg\n            viewBox="0 0 16 16"\n            xmlns="http://www.w3.org/2000/svg"\n            class="expand-collapse-glyph"\n        >\n            <path\n                d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"\n            />\n        </svg>\n    '}),Ki=rr.TreeView.compose({baseName:"tree-view",template:rr.treeViewTemplate,styles:(e,t)=>Br.css`
    ${(0,ae.display)("flex")} :host {
        flex-direction: column;
        align-items: stretch;
        min-width: fit-content;
        font-size: 0;
    }

    :host:focus-visible {
        outline: none;
    }
`}),Qi={jpAccordion:Rr,jpAccordionItem:Nr,jpAnchor:Yr,jpAnchoredRegion:Kr,jpAvatar:oa,jpBadge:aa,jpBreadcrumb:la,jpBreadcrumbItem:sa,jpButton:$a,jpCard:ya,jpCheckbox:ka,jpCombobox:Da,jpDataGrid:La,jpDataGridCell:ja,jpDataGridRow:Ha,jpDateField:_a,jpDialog:qa,jpDivider:Ua,jpListbox:Za,jpMenu:Ja,jpMenuItem:Qa,jpNumberField:oi,jpOption:ai,jpProgress:li,jpProgressRing:ni,jpRadio:ci,jpRadioGroup:hi,jpSearch:xi,jpSelect:vi,jpSlider:yi,jpSliderLabel:Vi,jpSwitch:Di,jpTab:ji,jpTabPanel:Bi,jpTabs:Li,jpTextArea:Ri,jpTextField:Mi,jpToolbar:_i,jpTooltip:qi,jpTreeItem:Ji,jpTreeView:Ki,register(e,...t){if(e)for(const o in this)"register"!==o&&this[o]().register(e,...t)}}},899:(e,t,o)=>{o.d(t,{i:()=>r});const r={horizontal:"horizontal",vertical:"vertical"}},586:(e,t,o)=>{var r;o.d(t,{N:()=>r}),function(e){e.ltr="ltr",e.rtl="rtl"}(r||(r={}))},655:(e,t,o)=>{function r(e,t,o,r){var a,i=arguments.length,l=i<3?t:null===r?r=Object.getOwnPropertyDescriptor(t,o):r;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)l=Reflect.decorate(e,t,o,r);else for(var n=e.length-1;n>=0;n--)(a=e[n])&&(l=(i<3?a(l):i>3?a(t,o,l):a(t,o))||l);return i>3&&l&&Object.defineProperty(t,o,l),l}o.d(t,{gn:()=>r})}}]);