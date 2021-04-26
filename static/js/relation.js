


import RelationChart from 'relation-chart'

// 容器
let element = document.querySelector('#map');

// 关系图数据

let data = {
    nodes: [
        {
            "name": "路人甲",
            "avatar": "./img/140646844806.jpg"
        },
        {
            "name": "路人乙",
            "avatar": "./img/141611471224.jpg"
        },
        {
            "name": "路人丙",
            "avatar": "./img/140848800133.jpg"
        },
    ],
    links: [
        {
            "source": 0,
            "target": 1,
            "relation": "朋友",
            "color": "734646"
        },
        {
            "source": 1,
            "target": 2,
            "relation": "女朋友",
            "color": "734646"
        },
    ],
}

// 创建人物关系图 svg
new RelationChart(element, data)