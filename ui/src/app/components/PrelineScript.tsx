"use client";

import {usePathname} from "next/navigation";
import {useEffect} from "react";

import {IStaticMethods} from "preline/preline";
import _ from 'lodash';
import Dropzone from 'dropzone';

declare global {
    interface Window {
        HSStaticMethods: IStaticMethods;
        _: typeof _;
        Dropzone: typeof Dropzone;
    }
}

export default function PrelineScript() {
    const path = usePathname();

    useEffect(() => {
        const loadPreline = async () => {
            await import("preline/preline");
            window._ = _;
            window.Dropzone = Dropzone;
            window.HSStaticMethods.autoInit();
        };

        loadPreline();
    }, [path]);

    return null;
}