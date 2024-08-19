"use client";

import {SyntheticEvent} from "react";

interface TitleProps {
    name: string;
    id: string;
    onItemClick?: (id: string, e?: SyntheticEvent) => void;
}

const Title = ({name, id}: TitleProps) => {
    const handleClick = () => {
        console.log(id)
    }
    return (<span className="text-sm text-gray-800 dark:text-neutral-200" onClick={handleClick}>
                  {name}
                </span>);
}

export default Title;