# 🖋️ The Weather Scribe  
---

## 🌦️ Project Description

**The Weather Scribe** ‘writes’ data, updating the weather and air quality data every hour and completing a full daily weather report in text on paper. The system combines motor control with a mechanical structure to automate the writing process. It is equipped with a paper feeding mechanism that automatically advances the paper after each section is completed. The project presents digital ecological data through physical writing to enhance public awareness and understanding of climate and environmental changes.

It is designed to be:
- 🪶 Low-cost
- ♻️ Sustainable  
...while maintaining robustness and automation.

---
## 📷 Project Preview
### Overview
<p align="center">
<img src="/ReadmeSrc/img/The Weather Scribe.jpg" width ="500">   
</p>

### Demonstration
<p align="center">
  <video src="https://github.com/user-attachments/assets/0c971a71-63dc-440f-b4bb-f69c3ff8ddf2">
  </video>
</p> 

### Output View
<p align="center">
<img src="./ReadmeSrc/img/Output.jpg" width ="500">   
</p>

---

## 🎯 Key Features

- 📡 Real-time environmental data collection (PM2.5, CO₂, temperature, humidity, wind, rain, etc.)
- 🧠 Structured weather summary generation
- ✍️ SVG to G-code conversion for physical writing
- 📈 Hourly updates and daily headers
- 🖨️ Pen plotter (GRBL-based CNC) output
---
## 📦 Component List

### ⚙️ Hardware List
| Component | Model / Specification | Purpose |
|-----------|-----------------------|---------|
| Writing Machine Control Board| [Arduino UNO](https://thepihut.com/products/arduino-uno-rev-3) | The control board for writing part|
| Motor Driver Board | [CNC Shield](https://www.amazon.co.uk/UMTMedia%C2%AE-CNC-Shield-V3-Expansion/dp/B09988FLR2/ref=sr_1_4?crid=133RBCSLNAQIR&dib=eyJ2IjoiMSJ9.jDTLrkdp6bStKsP6BfCSQtOMvUihUhgmIfajDIRRSkA0tyEy_INzMWBvBHhRslNbgCC5K_-8Q7919oJG-NEIauTR5nw0uLzNJesGnMPqomTuQKvqtJJh5v5kFp6m4HbEMf5wvlwXLlm7H19cmxDNaUVe_eNIUGdv6b-rvAo-ldbxoFfRTux4GdZ8ZG8BxdeD77pcIB_ARdLiezlkzOb69YMZ8m_4bmT-z3nBcXVpl6SOSYEyHaT7fXDhH46KaHRuzEoRYRFA_r-Cyckdok68QKCkpFwB1dcrXqqK-LPjJRU.sL3aqW_ujwY1UaBXhPukirwBGk1_vEh7M4C4uyMd-Uw&dib_tag=se&keywords=CNC+Shield&qid=1754921526&sprefix=cnc+shield%2Caps%2C109&sr=8-4) | Expansion board for Arduino Uno |
| Stepper Motor Driver | [A4988 driver modules X 4](https://www.amazon.co.uk/Stepstick-Stepper-Printer-Suitable-Arduino/dp/B07XRF8YPX/ref=sr_1_2?crid=31G0N7VEDIU24&dib=eyJ2IjoiMSJ9.RViRxrH8nS3p9GY34si5cHnRxwbaGkshnwsghs5LXPtiBOK8MJ4esAgm_tV1g3lc7HbUem_KvC4RmF7k-poLOsV5fsHX-HmjdLQjyAdVGOL2WxJ4p18xoWLf75k8cK7lCtezgL_MbeCKCey90wiBGQoLWepxcYPeQXV-corvoDmkYSStXNO2AahxEEt-IdCbP0D-2_BVv8pX1itJDQEy-WyNyTOdrXSsy9y2myda4LAm0_jMySYEBy788qhu6RHj6VBPlZos6cLDMN9tmlDTNLBdGOTx8EhodvTwcY8nrNg.FeEjQb1MmLhcdtD5-h5Rpzo00N8rLeq8UPhMGkyPfhU&dib_tag=se&keywords=A4988+driver+modules&qid=1754921567&sprefix=a4988+driver+modules%2Caps%2C96&sr=8-2)| Drive the Stepper motor|
| Stepper Motors | [NEMA 17 X 4](https://www.amazon.co.uk/dp/B07PMWQ21T?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1) | X/Y axis movement |
| Servo Motor | [SG90](https://www.amazon.co.uk/Helicopter-Airplane-Control-Compatible-Arduino/dp/B0DS63NMYZ/ref=sr_1_6?dib=eyJ2IjoiMSJ9.bnM-LzGGHHu8hTmUkKp5wbSwTL1bi0bLBHNagCAIFTYEQx5c90BHYToIVzg6R48HJ2gduiuc7OZQ4E8gU67WoqBsEhlbj0QyCmnEVJcQ_aLXHZF5FwyXj4ejaTVsn1I9Y0xWNx-z7zGf5B9saR4A55n9G5FItvDI_HyTEKQkf0nrNlIcmnBtn1PQuz8ihYsSWgxq-vzlMJGgnDojzdYiZXGhXwQowVRqhMx7Dx7QWbA_jWa8VzavcSCTvSlpYGz9G3tZi8au3QXv8H277-iWPcS4oLmXzLAqS6MCktn5AnU.VL6Pmxs96A1Tt_ECQmmApkbz64NguyQ9FJSzq6c8RB0&dib_tag=se&keywords=sg90&qid=1754921638&sr=8-6) | Lifts and lowers the pen |
| Power Supply | [12V 2A DC power](https://www.amazon.co.uk/Adapter-Converter-Driver-100-240V-Transformer/dp/B09DYDRFKZ/ref=sr_1_4?crid=1DAGVN0V8W38P&dib=eyJ2IjoiMSJ9.1-qIJKugLAB8tM1ZpK8aZkpIz9dCIudlnY2MQvzTlA5CU7iJmAAYU9rc_yVSTqbtcG7wNXHf85axZP30fvgKDQNM02s40sP0smjHbfJwOHi9VhVUliEN8QHqsdtovO1WxNoU0AjLTRuncVvUflpyzs_UCCzIeIAUcPIdchC71j9wnM5nwOjcBhE_yGczOyNWRmDaf0ebQ_fvV5sIOB0MQn2woz9TMu5oVgY4rhfS_BU.rOXJwkP4fP6G_gnV0J34XM4zRpSSQsYSSnd15PFxT7U&dib_tag=se&keywords=12v+2a+power+supply&qid=1754921665&sprefix=12v+2a%2Caps%2C78&sr=8-4) | Power for motors and electronics |
| Main Controller | [Raspberry Pi 4 Model B](https://thepihut.com/products/raspberry-pi-4-model-b) | System control and data processing |
| Environmental Sensor |[PM5003](https://thepihut.com/products/pms5003-particulate-matter-sensor-with-cable), [PM5003 connect board](https://thepihut.com/products/breakout-for-particulate-matter-sensor-pms5003), [USB to TTL Serial Cable](https://www.amazon.co.uk/CP2102-Serial-Converter-Module-Dupont/dp/B07XRF152K/ref=sr_1_13?crid=2XEDY5E4BLXY&dib=eyJ2IjoiMSJ9.1Ii5ef_QOkgHDGOdGF223sdz5zNtII4L-35shO5iKHZO2PtQJmzdJ9n0sqCNLXIqmcdv2hvjLbGw3wj5nWlxd7_OW3ujOnC9YOtSGTwN8c7exX3qBa3LFmjBgoo6JdWpIclQ1-lGXa-n_CyutZ_uU1blNGr4k3auajSrf9K_Cwk30WEQKVuwQfHVkaxX70bREvYewU_BlbEMzmPfYYa37_Pzw1qI3K2bnbmpCQqyPFSofdWxHeRLU8v0cKSF8SJNhyng-V-z3Hf0oTEy7yrbv-7Kty_PzH5umMO5KO9vxmo.s4ZOdryT0-nTNcErLPVJ-9PKferrfusWKLDsYOslxQI&dib_tag=se&keywords=USB+to+TTL+Serial+Cable&qid=1754922131&s=electronics&sprefix=usb+to+ttl+serial+cable%2Celectronics%2C87&sr=1-13), [SGP30](https://shop.pimoroni.com/products/adafruit-sgp30-air-quality-sensor-breakout-voc-and-eco2?variant=2089195110410)|  PM2.5 and eCO2 data collection |
|Switch Limit| [Switch Limit](https://www.amazon.co.uk/InduSKY-Switch-Momentary-Roller-Switches/dp/B08734MSDD/ref=sr_1_6?dib=eyJ2IjoiMSJ9.VtVvHW7Y65XI5ukA3XU6DtqCqpnItIMPnzohfR3sFsXwxreAGAhzC-0zlqYWLwBfIEaB2Wv46GKv5gcvop9XzpJFGtxvCipYjCwOQiRLVTW0ig8V81Big5X0aa13H_gZPhw0PJePK0ValY19Vgcq5ZWMVqaZvgFwhMQbCR0JHp8gCrJmZpv1eEGFAthRN_ttt3F0c3p8xhBGzVDo2ocpkiuyliZyFnJlZuiCjdNbeFbopwI_mTqn1g7nOXaiExHP_1BMYqcvuTUnT85sTRXdvHVzRHHHKmiZuCoGVixr2DQ.EMIozQTQT-MDbIFxyiqc1fH6KSwHeipsxubrPBZfQsQ&dib_tag=se&keywords=switch+limit&qid=1754922565&sr=8-6)| Zeroing and positioning|
|Wooden Baseboard| [Hardwood Plywood](https://www.cutmy.co.uk/wood/plywood-sheets/hardwood/)| Select the suitable board size(in this project is 600mm * 600mm *18mm)| 
| Foam Board  |[Foam Board](https://www.amazon.co.uk/Aselected-210X297Mm-Polystyrene-Project-Wedding/dp/B0C5CMML9V/ref=sr_1_6?adgrpid=163578048920&dib=eyJ2IjoiMSJ9._uO5vFB0ndNGpma0NhcKRTn6Fd48X7zumz9TTKBmiyU6W05YuVNMwGCYtSndzeh9RmKCjnw5lFwNjEdMLDsBKAZXFrlYk3lDKE4K4kCcsenGxtPw0efK8WcjbdwHseuqCZkaQoq-pVa0dG2sFSA0l87nPnZe9jq37CRbkmwoFDUJnGVaOGpvtEQFIh76Mbowki-Lu5uRKkkKEe4cGaYYHEj3JOBrptVjtgcWuT5luNqvO_AZjd36n8RIzdpjY4LoHblvlXHrJOrFzUoSRNUTbW8vi4Bqs96aXg-AoNQawwE.mbOM--PWO4l95yHgdRin1glZibDBLMnP2IaSpuwzdCk&dib_tag=se&gad_source=1&hvadid=696852751643&hvdev=c&hvexpln=69&hvlocphy=9044962&hvnetw=g&hvocijid=14403855840578661842--&hvqmt=e&hvrand=14403855840578661842&hvtargid=kwd-12560540&hydadcr=28145_2253864&keywords=foam%2Bboard&mcid=21320a04c7ea3cd7bbb4bf4b2e00cd8f&qid=1755104808&sr=8-6&th=1)| Soft base layer for writing paper, also can be cut to get custom size|
| Linear shaft |[Optical shaft](https://www.amazon.co.uk/EsportsMJJ-Diameter-Length-Cylinder-Optical/dp/B07MV83GXB?pd_rd_w=6ldwW&content-id=amzn1.sym.1af7ccf4-3158-4e8c-8fc4-62cb5b6b11e9&pf_rd_p=1af7ccf4-3158-4e8c-8fc4-62cb5b6b11e9&pf_rd_r=RYPCVN791XBAN7TRVY8E&pd_rd_wg=aPzMh&pd_rd_r=d3d4484d-61ab-4df1-bc25-36f258b724a6&pd_rd_i=B07MV83GXB&ref_=pd_bap_d_grid_rp_0_1_ec_pd_hp_d_atf_rp_4_t&th=1) ,[M8 threaded rod](https://www.amazon.co.uk/dp/B0BK4VDSFV?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1) | Based on the demand, purchase suitable numbers of linear shaft and cut the suitable length|
| Others | Wires, [DC Power Pigtails Cable](https://www.amazon.co.uk/Pigtails-Insulating-Female-Replacement-Security/dp/B0F4RK2YH1/ref=sr_1_7?crid=IOUCNH2CYPVY&dib=eyJ2IjoiMSJ9.tVQJoy0qBXwq_aAh1dljvu6a2qEjppG-Wkis-EtURrJY_dTqmlIxChZ9ckRnmbhA8toKsYh5VGSfw93awYvjBLnoi5loTQoeF9Rwz77JZsEKyoDL4FLw3NZiY9aujLdLl4spyYSzMwyoeugT5KwNcS3GBUq394zG8hb_qIBBYm21DCRgS1yxMT4x2WZmOAcG8sRsruE7uaG-xRXmzsosNhrMztkraH5OTxrQZwnln5K2i4F3U0kNnw9pH8zv3AUtnoggMDx0U-r_ATWR_lY4E8CD7Ewseig11Dx-b2FsWLg.FVqbrzjHYN7ZbCRUweYHCfVVC2aiwTqFTMWjlNxQqYo&dib_tag=se&keywords=DC%2BPower%2BPigtail%2BCable&qid=1754923818&s=industrial&sprefix=dc%2Bpower%2Bpigtail%2Bcable%2Cindustrial%2C78&sr=1-7&th=1),[M3 bolts](https://www.amazon.co.uk/Assortment-Stainless-Replacement-Machine-Fastener/dp/B0B3MGZ7T2/ref=sr_1_6?crid=30SCY3CVW3C9F&dib=eyJ2IjoiMSJ9.aLixtZwN3TilGBzrkJYybAY8UacezD49dcX991l75i_Kl7VWLpxenKNT_8uKoffDCq0J5yQ3E07PhQJPe4MYIyO_d9IV99lps6oM7S80FBP-mdjWhmg2OWKYZhZ69SjlnywiAMH0tOr0b75ehcshmQBPeIwFfqUzwubMVDtmHHfnek2ZAvXKIHqnnor0V004eE9DZb2gMABKR54TyJ15J_s6ryznnYj9ChsmO191Dg8qpy-TI7uxHpmqZOIRG1KP7Pj_Tz326ICuBSlNU-Wd-CLE5QMKAurhDan54XSZke4.UJQjJxvKw8NRcKGQKlrrq4Drvq8HI-k7mtcIdRg_52A&dib_tag=se&keywords=m3%2Bbolts%2Band%2Bnuts%2Bset&qid=1754923604&sprefix=M3%2Bbolts%2B%2Caps%2C59&sr=8-6&th=1), [M3 nuts](https://www.amazon.co.uk/TERF-Hexagon-Steel-Full-Nuts/dp/B09MDJHJTB/ref=sr_1_6?crid=1OMFH9FM6AYD2&dib=eyJ2IjoiMSJ9.mMaajKTgNRFmtFRqES95ZOmQKpQpbFQoGJbS8XGDQeQVnt8V6JF_VEeUL-SrrqFHvVLUKuRygEtYcIuaCXIATbmnj2GqfHIQsDA4Lcy85iGLO3xAVeX3oyrrnMimZmlN3b_rNGHDd8bhGLtn5r1H9qDBUnXsf1EhKSHyfAOokdCqQfSj1u8mzIT4_X3nffhk-pNm9v4Zt-O4aKJ7EB7DTQonXJCwUYVQeEMfhValbDFvpGxfSq3vWja8wmtzC8VI9D2uSXd_O5yxp0yfx3tnSj3DNWy5kJgKZ5zo6kAhuVg.Pvlc9VU8GdM-0EQv3-0IoIXuQNPBqCzty94lIPybj64&dib_tag=se&keywords=m3%2Bnuts&qid=1754923680&sprefix=m3%2Bnuts%2B%2Caps%2C101&sr=8-6&th=1), [Drawing Paper Roll](https://www.amazon.co.uk/Drawing-Paper-Durable-Bulletin-Paints/dp/B0D73W6XVP?pd_rd_w=Ml9zC&content-id=amzn1.sym.1af7ccf4-3158-4e8c-8fc4-62cb5b6b11e9&pf_rd_p=1af7ccf4-3158-4e8c-8fc4-62cb5b6b11e9&pf_rd_r=4993BEFXTWPYH99Q65GS&pd_rd_wg=NeGne&pd_rd_r=a4e7dd8d-5f09-4015-bb34-fe7702a8753c&pd_rd_i=B0D73W6XVP&psc=1&ref_=pd_bap_d_grid_rp_0_1_ec_pr_pd_yo_rr_rp_d_sccl_1_1_i), [Pen](https://www.amazon.co.uk/dp/B0CT3JS59T?ref=nb_sb_ss_w_as-reorder_k0_1_3&amp=&crid=2FS6N1F7892DD&sprefix=pen&th=1), [M8 nuts](https://www.amazon.co.uk/dp/B01BWLNTJE?ref=ppx_yo2ov_dt_b_fed_asin_title), [LM8UU Linear Bearing(24 mm length)](https://www.amazon.co.uk/sourcing-map-Bearing-Bearings-Packaging/dp/B0DP2KQTXZ/ref=sr_1_4_pp?crid=3CMG8NATNJ4AQ&dib=eyJ2IjoiMSJ9.fYevm3dM4JspnD1RXkpY3wderENAk9OqcNkgGhvR05N3ixIn2aBLGhkXxCnn65k7bfppMjLS7MGZugUlPQ0Sih53r5nLgeU8cW03mXhZK--Ra8FtDJu-UkO1Cff3oYRzeLzuVA03Kk3wgymCd8vkOnyNmn0DAcjc1xpEPoFzgOuFrLQJkbXvoSr0Z3BknmmdINsXQeVtYoWhzBOdpdHbCmBhhdPM56KmZkxlADlqfNDvDB0ahhQ0Vp5g9jhmS1J4ZBkOINf9zbOnocXbt_qGnw0e1Uhn5bVUiBCDpM5IURo.EEzh0vm9xSi4f2Obap0czbZ9BTOM7EprJ84IjOxdnaE&dib_tag=se&keywords=LM8UU&qid=1754924065&s=industrial&sprefix=lm8uu%2Cindustrial%2C100&sr=1-4), [LM8UU Linear Bearing(45 mm length)](https://www.amazon.co.uk/sourcing-map-Linear-Bearings-Length/dp/B07H958LGN/ref=sr_1_1?crid=THI20RTL8RO4&dib=eyJ2IjoiMSJ9.zj8ZSo_3Ykwx25dqfXoth7tpEdOv9grMiN2LTvM6Dvaaab7hgZFkd4OHsUHDUF_lZPFOy8zS0BraS6wb25Qn4S8_aoZa4nEMJPJm8A08yHKFx17X3FG3e9m_edTE7Y_heJmVZ49HPnfaGOiVXprQEv19Vh-v7VmfTQnPJs00EkkLBd6EgCqdWyqIBGUNbGb5nNld3PEdxCFg27EzrdJ8RoRG4pIFc6wDF6KSm58W6iRzQ0UTgasixdERdDizeArjP4Y6nARSbL583-mfCcYbZLMmkiW52jkvzoGF7ixI1q0.7K1Lw9u0Fw-1mFvXmb-nvncHm-UjwNsbW9ZV0TmERxQ&dib_tag=se&keywords=LM8UU%2B45mm&qid=1754924274&s=industrial&sprefix=lm8uu%2B45mm%2Cindustrial%2C67&sr=1-1&th=1),[6mm Width GT2 Timing Belt](https://www.amazon.co.uk/DollaTek-Timing-Reprap-Printer-Rostock/dp/B07DK1PPDV/ref=sr_1_8?crid=2IKYW85VNT53L&dib=eyJ2IjoiMSJ9.sFDE908EBasUZdaQSOXZvaPKrVceF21nm_iNWWzJhlKIVaV9VtqVyH1n8OZj-IAFGnLcJbEPgUsXin6PBc1x7K0JHaGEuD-9xUBwVjuXvDSKK51-gPMauPF1PCJtFWvBcObY1tzLWf9EfMGgFlEYSirvhh7gzccd7ViMyj9L1FdGOaYAYORSQ0jd0qhcLULfKdHi9bdM-X6yA19WLXkfs-Ahg-c5L6pVni8A8uJEet1Sjh4Nxgp_DKnSPxDdXDiD2--J3RBjfkeKDbimjiqrqLGgpUQT4k5NZp3PppgDaug.rbCBMauDsbK4xwq_WwpfLCTauWh5zgJAqKmUVWOZD-I&dib_tag=se&keywords=gt2+belt+6mm&qid=1754924435&sprefix=belt+gt%2Caps%2C117&sr=8-8), [GT2 Bore Timing Pulley](https://www.amazon.co.uk/dp/B09VPRVD46?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1), [GT2 Idler Pulley](https://www.amazon.co.uk/dp/B0CD2494K4?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1), [Cable-Core Spiral Binding](https://www.amazon.co.uk/dp/B003CL4Y9C?ref=ppx_yo2ov_dt_b_fed_asin_title), [Elastic Bands (for pen holder)](https://www.amazon.co.uk/dp/B0DMSFNQNW?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1), [M5 bolts](), [M5 nuts]()| Assembly component |

### 🧩 3D Printed Parts
#### 🧩 Online-sources-designed 3D Printed Parts
##### 🔹 Models from Cults3D (by AKASHKUMAR)

| Part Name                                | Source Link                                                                 |
|------------------------------------------|------------------------------------------------------------------------------|
| Pen Holder                                         | [Cults3D Model](https://cults3d.com/en/3d-model/gadget/diy-pen-plotter-machine-writing-machine)                                                                      |
| Writing Machine Controller Box                     | ↑ same                                                                       |
| Writing Machine Pen Slider                         | ↑ same                                                                       |
| Writing Machine Slider X axis                      | ↑ same                                                                       |
| Writing Machine Slider Y axis                      | ↑ same                                                                       |
| Writing Machine Stepper Motor Holder Y axis        | ↑ same                                                                       |
| Writing Machine X axis End                         | ↑ same                                                                       |

##### 🔹 Models from Thingiverse (by Skimbal)

| Part Name                | Source Link                                      | Note
|--------------------------|--------------------------------------------------| -------------|
| Drag Chain Segment       | [Thingiverse](https://www.thingiverse.com/thing:915487) | Hide the wires|
| Chain Mount Bracket      | ↑ same                                           | ↑ same                                           |


##### 🔹 Model from MakerWorld (by THEMAKERGUY)

| Part Name              | Source Link                                                                 |
|------------------------|------------------------------------------------------------------------------|
| Raspberry Pi 4 Case    | [MakerWorld](https://makerworld.com/en/models/62316-raspberry-pi-4-model-b-case) |

##### 🔹 Model from Printables (by Neophob)

| Part Name        | Source Link                                                                 |
|------------------|------------------------------------------------------------------------------|
| M5 Thumb Screw   | [Printables](https://www.printables.com/model/711250-knob-thumb-screw-m2-m3-m4-m5-m6-socket) |  


#### 🧩 Self-designed 3D Printed Parts
| Part Name                              | File Path                                  | Notes                       |
|----------------------------------------|--------------------------------------------|------------------------------------------|
| Gear                                   | [model/Gear.stl](./model/Gear.stl)           | Paper feed drive gear                   |
| Paper Channel                          | [model/Paper channel.stl](./model/Paper%20channel.stl) | Guides paper to writing area      |
| PM2.5 and eCO₂ Sensor Enclosure        | [model/PM2.5 and eCO2 sensor enclosure.stl](./model/PM2.5%20and%20eCO2%20sensor%20enclosure.stl) | Sensor mounting box              |
| Roller End Cap (Paper Collection)      | [model/Roller end cap for paper collection part.stl](./model/Roller%20end%20cap%20for%20paper%20collection%20part.stl) | Supports paper take-up roller   |
| Roller End Cap (Roll Paper)            | [model/Roller end cap for roll paper.stl](model/Roller%20end%20cap%20for%20roll%20paper.stl) | For feed roller ends             |
| Sliders for A Axis                     | [model/Sliders for the A axis.stl](./model/Sliders%20for%20the%20A%20axis.stl) | Linear guide slider for writing arm     |
| Stepper Motor Support (Axis)         | [model/Stepper motor support for A axis.stl](./model/Stepper%20motor%20support%20for%20A%20axis.stl) | Motor mounting bracket         |
| Support for Paper Collection           | [model/Support for paper collection part.stl](./model/Support%20for%20paper%20collection%20part.stl) | Holds roller below writing surface      |
| Support for Roll Paper                 | [model/Support for roll paper.stl](./model/Support%20for%20roll%20paper.stl) | Base for holding paper feed roll        |
| Support for A Axis                     | [model/Support for the A axis.stl](./model/Support%20for%20the%20A%20axis.stl) | Structural support for horizontal arm   |

#### The main structure (eg.X/Y frame, sliders, pen holder, motor mounts) can be assembled by following the [video](https://www.youtube.com/watch?v=w1urQnTpvn0) of Creativity Buzz. Additional parts designed for this project—such as sensor mounts, paper rollers, and supports—can be installed according to their positions in the final build [photo](https://github.com/mk20661/The_Weather_Scribe/blob/main/ReadmeSrc/img/The%20Weather%20Scribe.jpg)

---

## 🔌 Circuit Connections
### The Circuit Connection of the Writing Machine
<p align="center">
<img src="/ReadmeSrc/img/writingmachine.png" width ="800">   
</p>

### The Sensor Connection with Raspberry Pi 4B
<p align="center">
<img src="/ReadmeSrc/img/ciritut for pi 4.png" width ="800">   
</p>

### After these two circuit connection finishing, use the arduino uno cable to connect between Arduino UNO and Raspberry Pi

## 💾 Upload GRBL Firmware to Arduino Uno 
After connecting all circuits and assemble all the components, follow the steps below to   upload **GRBL** firmware to Arduino Uno. 
### 📦 1. Install Arduino IDE
Download and install the Arduino IDE from the [official website](https://www.arduino.cc/en/software)

### 🔧 2. Add GRBL Library
This project already includes the path of GRBL firmware source in: **GRBL/grbl**

To make this library available to the Arduino IDE:

1. Locate the path above in File Explorer  
2. Copy the entire `grbl` folder  
3. Paste it into your Arduino libraries folder, typically located at: Documents\Arduino\libraries\


After copying, your structure should look like:

```
Documents\Arduino\libraries\grbl
|- config.h
|- cpu_map.h
|- grbl.h
|- ...
```

### 🛠️ 3. Upload GRBL Firmware to Arduino Uno

1. Launch the **Arduino IDE**  
2. Go to: File → Examples → grbl → grblUpload
3. Select the correct board and port:
```
Tools → Board: Arduino Uno
Tools → Port: COMx (your Arduino's COM port)
```
4. Click the **Upload** button (✔️)

Once complete, the Arduino Uno will be flashed with GRBL firmware and ready to accept G-code commands via serial.

---

### ✅ 4.Verify GRBL Installation

1. Open the **Serial Monitor** (top-right magnifying glass icon)  
2. Set the **baud rate to 115200**  
3. You should see, like this:

```
Grbl 0.9h ['$' for help]
```

### ⚙️ 5. Configure GRBL Settings via Serial Monitor
This project includes a GRBL configuration file located at: **GRBL/GRBL Config.txt**

```
Each line in this file is a GRBL setting command, such as:
$0=10 (step pulse, usec)
$1=25 (step idle delay, msec)
$2=0 (step port invert mask:00000000)
$3=3 (dir port invert mask:00000011)
.....
```
## 🔧 Installation Instructions on Raspberry Pi 4B
After connecting all circuits and assemble all the components, follow the steps below to set up and run **The Weather Scribe** on a Raspberry Pi 4 Model B.
### 📦  System Requirements

- Raspberry Pi 4B (2GB or more)
- Raspberry Pi OS (Bookworm or Bullseye, 64-bit recommended)
- Internet connection (for API and MQTT)
- Python 3.9+

### 🧬 Clone the Repository
```
git clone https://github.com/mk20661/The_Weather_Scribe.git
cd The_Weather_Scribe
```

### 🧪 Create Python Virtual Environment
```bash
cd The_Weather_Scribe
python3 -m venv weather_scribe_env
source weather_scribe_env/bin/activate
```
### 🦀 Install Rust and Cargo on Raspberry Pi

To compile `svg2gcode`, Rust and Cargo are required. Follow the steps below to install:

```bash
curl https://sh.rustup.rs -sSf | sh
source $HOME/.cargo/env
cargo --version
```
### 📦 Install Python Dependencies
```
cd The_Weather_Scribe/main/piCode
pip install -r requirements.txt
```
### 📦 Install svg2gcode-cli
This tool is based on the [`svg2gcode`](https://github.com/sameer/svg2gcode) project by [sameer](https://github.com/sameer), which converts SVG files into G-code for CNC plotting.  
```
cargo install svg2gcode-cli
```
### ✨ Run the script
```
cd The_Weather_Scribe/main/piCode
python main.py
```
### ✨ Enable startup script for booting up
``` bash
# write the startup script
nano writingMachine_start.sh

export PATH="$HOME/.cargo/bin:$PATH"
export CARGO_HOME="$HOME/.cargo"
cd The_Weather_Scribe # entry the location of clone
source weather_scribe_env/bin/activate # entry the path for installing the virtual environment
python main.py >> /home/pi/startup.log 2>&1

# Save the script and then grant authority to the script
chmod +x /home/pi/writingMachine_start.sh

# Set up the startup through crontab
crontab -e
# Add at the last line
@reboot /home/pi/writingMachine_start.sh>> /home/pi/startup.log 2>&1
```

### 🔄 Workflow
<p align="center">
<img src="/ReadmeSrc/img/workflow.jpg">   
</p>

## Reference
 ```
1. AKASHKUMAR (2024). DIY Pen Plotter Machine | Writing Machine. [online] Cults 3D. Available at: https://cults3d.com/en/3d-model/gadget/diy-pen-plotter-machine-writing-machine [Accessed 11 Jun. 2025].
2. Creativity Buzz (2023). Writing Machine Robot Science Project | Arduino Project for Beginners. [online] YouTube. Available at: https://www.youtube.com/watch?v=w1urQnTpvn0 [Accessed 1 June 2025].
3. TuxSoft (2017). Drag Chain with mounts. [online] Thingiverse. Available at: https://www.thingiverse.com/thing:915487 [Accessed 11 Jul. 2025].
4. Misosiru (2025). Raspberry pi 4 Model B case by misosiru MakerWorld: Download Free 3D Models. [online] Makerworld.com. Available at: https://makerworld.com/en/models/62316-raspberry-pi-4-model-b-case [Accessed 11 Jun. 2025].
5. Olekhal (2024). Knob thumb Screw M2-M3-M4-M5-M6 socket. [online] Printables.com. Available at: https://www.printables.com/model/711250-knob-thumb-screw-m2-m3-m4-m5-m6-socket [Accessed 11 Jun. 2025].
6. Sameer (2024). GitHub - sameer/svg2gcode: Convert vector graphics to g-code for pen plotters, laser engravers, and other CNC machines. [online] GitHub. Available at: https://github.com/sameer/svg2gcode [Accessed 8 Jul. 2025].
```
