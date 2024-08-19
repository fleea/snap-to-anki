type TreeDataType = "png" | "jpg" | "pdf";

export interface TreeData {
    id: string;
    name: string;
    type?: TreeDataType;
    children?: TreeData[];
}

export interface TreeViewProps {
    data: TreeData[];
}

export const defaultData: TreeData[] = [
    {
        id: "1",
        name: "Nederlands: Nieuw Nederlands 2",
        children: [
            {
                id: "1-1",
                name: "Hoofdstuk 1: Lezen en Schrijven",
                children: [
                    {id: "1-1-1", name: "Paragraaf 1.1: Begrijpend Lezen"},
                    {id: "1-1-2", name: "Paragraaf 1.2: Creatief Schrijven"},
                    {id: "1-1-3", name: "Paragraaf 1.3: Grammatica"}
                ]
            },
            {
                id: "1-2",
                name: "Hoofdstuk 2: Spreken en Luisteren",
                children: [
                    {id: "1-2-1", name: "Paragraaf 2.1: Presentatietechnieken"},
                    {id: "1-2-2", name: "Paragraaf 2.2: Debatteren"}
                ]
            }
        ]
    },
    {
        id: "2",
        name: "Wiskunde: Getal & Ruimte 2 HAVO/VWO",
        children: [
            {
                id: "2-1",
                name: "Hoofdstuk 1: Vergelijkingen en Ongelijkheden",
                children: [
                    {id: "2-1-1", name: "Paragraaf 1.1: Lineaire Vergelijkingen"},
                    {id: "2-1-2", name: "Paragraaf 1.2: Kwadratische Vergelijkingen"},
                    {id: "2-1-3", name: "Paragraaf 1.3: Ongelijkheden"}
                ]
            },
            {
                id: "2-2",
                name: "Hoofdstuk 2: Meetkunde",
                children: [
                    {id: "2-2-1", name: "Paragraaf 2.1: Pythagoras"},
                    {id: "2-2-2", name: "Paragraaf 2.2: Goniometrie"}
                ]
            }
        ]
    },
    {
        id: "3",
        name: "Geschiedenis: Memo 2 Gymnasium",
        children: [
            {
                id: "3-1",
                name: "Hoofdstuk 1: De Middeleeuwen",
                children: [
                    {id: "3-1-1", name: "Paragraaf 1.1: Vroege Middeleeuwen"},
                    {id: "3-1-2", name: "Paragraaf 1.2: Hoge Middeleeuwen"},
                    {id: "3-1-3", name: "Paragraaf 1.3: Late Middeleeuwen"}
                ]
            },
            {
                id: "3-2",
                name: "Hoofdstuk 2: De Renaissance",
                children: [
                    {id: "3-2-1", name: "Paragraaf 2.1: Kunst en Cultuur"},
                    {id: "3-2-2", name: "Paragraaf 2.2: Wetenschappelijke Revolutie"}
                ]
            }
        ]
    },
    {
        id: "4",
        name: "Latijn: Via Nova 2",
        children: [
            {
                id: "4-1",
                name: "Hoofdstuk 1: De Romeinse Mythologie",
                children: [
                    {id: "4-1-1", name: "Paragraaf 1.1: Goden en Godinnen"},
                    {id: "4-1-2", name: "Paragraaf 1.2: Helden en Monsters"}
                ]
            },
            {
                id: "4-2",
                name: "Hoofdstuk 2: Grammatica",
                children: [
                    {id: "4-2-1", name: "Paragraaf 2.1: Naamvallen"},
                    {id: "4-2-2", name: "Paragraaf 2.2: Werkwoordsvormen"}
                ]
            }
        ]
    },
    {
        id: "5",
        name: "Natuurkunde: Newton 2",
        children: [
            {
                id: "5-1",
                name: "Hoofdstuk 1: Krachten en Beweging",
                children: [
                    {id: "5-1-1", name: "Paragraaf 1.1: Wetten van Newton"},
                    {id: "5-1-2", name: "Paragraaf 1.2: Zwaartekracht"}
                ]
            },
            {
                id: "5-2",
                name: "Hoofdstuk 2: Elektriciteit",
                children: [
                    {id: "5-2-1", name: "Paragraaf 2.1: Stroomkringen"},
                    {id: "5-2-2", name: "Paragraaf 2.2: Wet van Ohm"}
                ]
            }
        ]
    },
    {
        id: "6",
        name: "Biologie: Biologie voor Jou 2",
        children: [
            {
                id: "6-1",
                name: "Hoofdstuk 1: Cellen en Weefsels",
                children: [
                    {id: "6-1-1", name: "Paragraaf 1.1: Celstructuren"},
                    {id: "6-1-2", name: "Paragraaf 1.2: Celprocessen"}
                ]
            },
            {
                id: "6-2",
                name: "Hoofdstuk 2: Ecologie",
                children: [
                    {id: "6-2-1", name: "Paragraaf 2.1: Ecosystemen"},
                    {id: "6-2-2", name: "Paragraaf 2.2: Voedselketens"}
                ]
            }
        ]
    }
];